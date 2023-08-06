"""
Supporting class for oras bundle plugin
"""
import json
import os
import platform

from datetime import datetime
from http import cookiejar

import jsonschema
import oras.defaults
import oras.oci
import oras.provider
import oras.schemas
import requests

from oras.container import Container
from oras.decorator import ensure_container

import hoppr


class Registry(oras.provider.Registry):
    """Override the default Oras Registry Class"""

    @ensure_container
    def push(self, container: Container, archives: list, logger):  # pylint: disable=W0221
        """
        Given a list of layer metadata (paths and corresponding mediaType) push.
        """
        # Prepare a new manifest
        manifest = oras.oci.NewManifest()
        self.session.cookies.set_policy(BlockAll())

        self.upload_blobs(container, archives, manifest, logger)

        # Prepare manifest and config (add your custom annotations here)
        manifest["annotations"] = {
            "org.opencontainers.image.created": str(datetime.now()),
            "ArtifactType": "Oras OCI Bundle",
            "Documentation": "https://oras.land/cli/",
        }
        config_file = "/tmp/oras-conf.json"
        config_blob = {'os': str(platform.platform()), 'HopctlVersion': hoppr.__version__}
        self.setup_default_config(config_blob, config_file)
        conf, config_file = oras.oci.ManifestConfig(
            path=config_file, media_type="application/vnd.oci.image.config.v1+json"
        )
        conf["annotations"] = config_blob

        # Config is just another layer blob!
        logger.info(f"Uploading config to {container.uri}")
        logger.info(f"Config {conf}")
        logger.flush()
        response = self.upload_blob(config_file, container, conf)
        self._check_200_response(response)
        os.remove(config_file)

        # Final upload of the manifest
        manifest["config"] = conf
        # Try updating the manifest
        response = self.upload_manifest(manifest=manifest, container=container)
        self._check_200_response(response=response)
        return response

    def upload_blobs(self, container: Container, archives: list, manifest: dict, logger) -> dict:
        """
        Upload individual layers to oci registry

        Args:
            container (Container): oras container
            archives (list): list of layers to upload
            logger (_type_): hoppr logger
        """
        # Upload files as blobs
        for item in archives:
            blob = item.get("path")
            media_type = item.get("media_type")
            annots = item.get("annotations") or {}

            if not blob or not os.path.exists(blob):
                logger.info(f"Path {blob} does not exist or is not defined.")
                continue

            # Artifact title is basename or user defined
            blob_name = item.get("title") or os.path.basename(blob)

            # Create a new layer from the blob
            layer = oras.oci.NewLayer(blob, media_type, is_dir=False)
            logger.info(f"Preparing layer {layer}")

            # Update annotations with title we will need for extraction
            annots.update({oras.defaults.annotation_title: blob_name})
            layer["annotations"] = annots

            # update the manifest with the new layer
            manifest["layers"].append(layer)

            # Upload the blob layer
            logger.info(f"Uploading {blob} to {container.uri}")
            logger.flush()
            response = self.upload_blob(blob, container, layer)
            self._check_200_response(response)
        return manifest

    def upload_manifest(self, manifest: dict, container: Container) -> requests.Response:
        """
        Read a manifest file and upload it.

        :param manifest: manifest to upload
        :type manifest: dict
        :param container:  parsed container URI
        :type container: oras.container.Container or str
        """
        self.reset_basic_auth()  # Should we really be reseting?
        jsonschema.validate(manifest, schema=oras.schemas.manifest)
        headers = {
            "Content-Type": oras.defaults.default_manifest_media_type,
            "Content-Length": str(len(manifest)),
        }
        hostname = ""
        if ':' in container.registry:
            hostname = container.registry.split(":")[0]
        else:
            hostname = container.registry
        put_url = f"{self.prefix}://{hostname}/v2/{container.api_prefix}/manifests/{container.tag}"
        response = self.do_request(put_url, "PUT", headers=headers, json=manifest)
        return response

    def setup_default_config(self, config_blob: dict, config_file: str):
        """
        Setup defualt oras object config
        """
        with open(config_file, "w", encoding='utf-8') as fout:
            json.dump(config_blob, fout, indent=4)


class BlockAll(cookiejar.CookiePolicy):
    """
    Block all cookies

    Args:
        cookiejar (CookiePolicy): _description_
    """

    return_ok = (  # type: ignore[assignment]
        set_ok
    ) = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False  # pylint: disable=C3001
    netscape = True
    rfc2965 = hide_cookie2 = False
