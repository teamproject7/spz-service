import base64
import os
import uuid

import magic

from src.const import ALLOWED_MIME, UPLOAD_FOLDER, MAX_IMAGE_FILE_SIZE


def allowed_file(filename):
    mime = magic.Magic(mime=True)
    if mime.from_file(filename) in ALLOWED_MIME:
        return True

    return False


def allowed_file_size(path):
    si = os.stat(path)
    b = si.st_size

    return b <= MAX_IMAGE_FILE_SIZE


def save_b64_to_file(b64_str):
    fname = str(uuid.uuid4())
    fpath = os.path.join(UPLOAD_FOLDER, fname)

    try:
        f = open(fpath, 'wb')
        f.write(base64.b64decode(b64_str))
        f.close()

        # TODO logg
        return fpath
    except:
        # TODO logg
        return False
