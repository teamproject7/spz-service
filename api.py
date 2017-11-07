import random
from spz_helper import generate_spzs, generate_spz_object
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

spz_count = 10 ** 2
SPZS = generate_spzs(spz_count)


def decision(probability):
    return random.random() < probability


def abort_if_spz_doesnt_exist(spz_string):
    if spz_string not in SPZS:
        abort(404, message="SPZ {} not found".format(spz_string), error_code='SPZ_NOT_FOUND')


parser = reqparse.RequestParser()
parser.add_argument('spz')


class SPZ(Resource):
    def get(self, spz_string):
        abort_if_spz_doesnt_exist(spz_string)
        return SPZS[spz_string]

    def put(self, spz_string):
        args = parser.parse_args()
        spz = generate_spz_object(args['spz'])
        SPZS[spz_string] = spz
        return spz, 201


api.add_resource(SPZ, '/spz/<spz_string>')

if __name__ == '__main__':
    app.run(debug=True)
