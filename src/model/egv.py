import uuid

from src.model.spz import *
import time

FIRSTNAMES = ["Aaren", "Aarika", "Abagael", "Abagail", "Abbe", "Abbey", "Abbi"]
LASTNAMES = ["Elladine", "Elle", "Ellen", "Ellene", "Ellette", "Elli", "Ellie", "Ellissa", "Elly", "Ellyn", "Ellynn",
             "Elmira", "Elna"]

COLORS = ['white', 'black', 'blue', 'red', 'green', 'orange', 'brown', 'grey', 'purple', 'violet']
BRANDS = ['Skoda', 'Audi', 'BMW', 'Honda', 'Kia', 'Volkswagen']
MODELS = ['Model I', 'Model II', 'Model III']
YEARS = list(range(1900, 2017))


def foo(plate):
    return {
        "id": str(uuid.uuid4()),
        "plate": plate['plate'],
        "coordinates": plate['coordinates'],
        "vehicle": {
            "id": str(uuid.uuid4()),
            "parameters": {
                "model": random.choice(MODELS),
                "brand": random.choice(BRANDS),
                "year": random.choice(YEARS),
                "color": random.choice(COLORS)
            },
            "owner": {
                "id": str(uuid.uuid4()),
                "pid": "OB123489",
                "fullname": "{} {}".format(random.choice(FIRSTNAMES), random.choice(LASTNAMES))
            },
            "insurance": {
                "company": "Prva poistovna",
                "date": time.time(),
                "valid": random.choice([False, True]),
                "message": "Nezaplatene poistenie"
            },
            "checks": {
                "stk": {
                    "date": time.time(),
                    "valid": random.choice([False, True])
                },
                "ek": {
                    "date": time.time(),
                    "valid": random.choice([False, True])
                }
            }
        }
    }


def generate_egv_object(alpr_res):
    plates = [foo(plate) for plate in alpr_res['results']]

    return {
        "processing_time_ms": alpr_res['processing_time_ms'],
        "data": plates
    }


def generate_spzs(count):
    spzs = {}
    while len(spzs) <= count:
        spz = generate_spz()
        if spz not in spzs:
            spzs[spz] = generate_egv_object(spz)

    return spzs
