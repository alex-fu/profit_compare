# coding=utf-8

import requests

from utils.uuid_utils import get_uuid


def download_file(url, filename=None):
    if filename is None:
        filename = get_uuid()

    uuid = get_uuid()
    print("downloading from {} to file {} ... -> uuid {}".format(url, filename, uuid))

    data = requests.get(url, stream=True)

    if data is not None and data.ok:
        with open(filename, "wb") as handle:
            handle.write(data.content)

        print("downloaded succeed! -> uuid {}".format(uuid))
    else:
        print("[ERROR]: download failed! -> uuid {}".format(uuid))

