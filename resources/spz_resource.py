import random
from flask_restful import reqparse, abort, Api, Resource
from egv_model import *
from storage import *


def decision(probability):
    return random.random() < probability


def accept_spz_and_persist(spz_string):
    new_egv_obj = generate_egv_object(spz_string)
    insert_spz(spz_string, new_egv_obj)
    persist()
    return new_egv_obj


def deny_spz_and_persist(spz_string):
    insert_spz(spz_string, None)
    persist()


def not_found(spz_string):
    abort(404, message="SPZ {} not found".format(spz_string), error_code='SPZ_NOT_FOUND')


class SPZ(Resource):
    def get(self, spz_string):

        found = find_spz(spz_string)

        if found is False:
            if decision(PROB_FOUND):
                return accept_spz_and_persist(spz_string)
            else:
                deny_spz_and_persist(spz_string)
                not_found(spz_string)

        if found is None:
            not_found(spz_string)

        return found

    def put(self, spz_string):
        # args = parser.parse_args()
        spz = generate_egv_object(spz_string)
        accept_spz_and_persist(spz_string)
        return spz, 201

    def delete(self, spz_string):
        # args = parser.parse_args()
        if spz_string in SPZS:
            SPZS[spz_string] = None

        return 201
