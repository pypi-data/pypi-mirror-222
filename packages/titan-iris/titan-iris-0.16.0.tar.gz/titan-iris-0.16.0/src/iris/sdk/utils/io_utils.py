"""This file contains the IO related helper functions for the Iris package."""
# ───────────────────────────────────────────────────── imports ────────────────────────────────────────────────────── #

import gzip
import io
import json
import tarfile
from logging import getLogger
from pathlib import Path

import requests
import wget
from tqdm import tqdm
from tqdm.utils import CallbackIOWrapper

from iris.sdk.exception import DownloadLinkNotFoundError

logger = getLogger("iris.utils.io_utils")

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                                       IO Utils                                                       #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #


def make_targz(local_folder_path: str):
    """Create a tar.gz archive of the local folder - make this deterministic / exclude timestamp info from gz header.

    Args:
        local_folder_path: The folder to be converted to a tar.gz

    Returns: A buffer containing binary of the folder as a tar.gz file

    """
    tar_buffer = io.BytesIO()
    block_size = 4096
    # Add files to a tarfile, and then by-chunk to a tar.gz file.
    with tarfile.open(fileobj=tar_buffer, mode="w") as tar:
        tar.add(
            local_folder_path,
            arcname=".",
            filter=lambda x: None if "pytorch_model.bin" in x.name else x,
        )
    # Exclude pytorch_model.bin if present, as safetensors should be uploaded instead.
    with gzip.GzipFile(
        filename="",  # do not emit filename into the output gzip file
        mode="wb",
        fileobj=tar_buffer,
        mtime=0,
    ) as myzip:
        for chunk in iter(lambda: tar_buffer.read(block_size), b""):
            myzip.write(chunk)

    return tar_buffer


def download_model(
    download_url: str,
    model_name: str,
    path: str = "model_storage",
    json_output: bool = False,
):
    """Helper function for iris download to download model to local machine giving download url.

    Args:
        download_url (str): url to download the model
        model_name (str): name of the model
        path (str, optional): path for model storage . Defaults to "model_storage".
        json_output (bool, optional): Whether to output the progress in json format. Defaults to False.

    Raises:
        DownloadLinkNotFoundError: Download link expired error
    """
    # download the tar file
    try:
        if json_output:
            tarfile_path = wget.download(download_url, path, bar=None)
            try:
                json.loads(tarfile_path)
            except json.JSONDecodeError:
                pass
        else:
            tarfile_path = wget.download(download_url, path)
    except Exception as e:
        raise DownloadLinkNotFoundError from e

    # Extract the tar file to a folder on the local file system
    with tarfile.open(tarfile_path) as tar:
        tar.extractall(path=f"model_storage/{model_name}/models")

    # delete the tar file
    Path(tarfile_path).unlink()


def upload_from_file(tarred: io.BytesIO, dst: str, json_output: bool = False):
    """Upload a file from src (a path on the filesystm) to dst.

    e Args:
         tarred (io.BytesIO): The file to upload. (e.g. a tarred file).
         dst (str): The url of the destination.
         Must be a url to which we have permission to send the src, via PUT.
         json_output (bool, optional): Whether to output the progress in json format. Defaults to False.

    Returns:
         Tuple[str, requests.Response]: A hash of the file, and the response from the put request.
    """
    if json_output:
        tarred.seek(0)
        response = requests.put(dst, data=tarred)
        response.raise_for_status()
        return response
    else:
        with tqdm(
            desc="Uploading",
            total=tarred.getbuffer().nbytes,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
        ) as t:
            tarred.seek(0)
            reader_wrapper = CallbackIOWrapper(t.update, tarred, "read")
            response = requests.put(dst, data=reader_wrapper)
            response.raise_for_status()
            return response
