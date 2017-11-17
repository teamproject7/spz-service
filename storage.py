import pickle
from const import *

SPZS = []


def init_storage():
    if not os.path.exists(DATA_DIRECTORY):
        os.makedirs(DATA_DIRECTORY)

    global SPZS
    SPZS = load_obj(path=SPZS_PICKLEPATH)


def persist():
    global SPZS
    save_obj(SPZS, SPZS_PICKLEPATH)


def insert_spz(spz_string, obj):
    SPZS[spz_string] = obj


def find_spz(spz_string):
    if spz_string in SPZS:
        if SPZS[spz_string] is not None:
            return SPZS[spz_string]
        else:
            return None
    else:
        return False


def save_obj(obj, path):
    with open(path, 'ab+') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(path):
    with open(path, 'rb+') as f:
        return pickle.load(f)
