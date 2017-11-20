import uuid

from src.model.spz import *

FIRSTNAMES = ["Aaren", "Aarika", "Abagael", "Abagail", "Abbe", "Abbey", "Abbi"]
LASTNAMES = ["Elladine", "Elle", "Ellen", "Ellene", "Ellette", "Elli", "Ellie", "Ellissa", "Elly", "Ellyn", "Ellynn",
             "Elmira", "Elna"]


def generate_egv_object(spz):
    return {
        'spz': spz,
        'owner': {
            'id': str(uuid.uuid4()),
            'firstname': random.choice(FIRSTNAMES),
            'lastname': random.choice(LASTNAMES)
        },
        'vehicle': {
            'color': 'red'
        }
    }


def generate_spzs(count):
    spzs = {}
    while len(spzs) <= count:
        spz = generate_spz()
        if spz not in spzs:
            spzs[spz] = generate_egv_object(spz)
            # else:
            # print(spz)

    return spzs
