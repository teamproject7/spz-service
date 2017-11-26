import base64
import os
import uuid

import magic

from src.const import ALLOWED_MIME, DATA_DIRECTORY


def allowed_file(filename):
    mime = magic.Magic(mime=True)
    if mime.from_file(filename) in ALLOWED_MIME:
        return True

    return False


def save_b64_to_file(b64_str):
    fname = str(uuid.uuid4())
    fpath = os.path.join(DATA_DIRECTORY, fname)

    try:
        f = open(fpath, 'wb')
        f.write(base64.b64decode(b64_str))
        f.close()

        # TODO logg
        return fpath
    except:
        # TODO logg
        return False
