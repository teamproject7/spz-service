from flask_restful import reqparse, Resource
from src.responses import AppResponses
from src.model.egv import create_egv_object

parser = reqparse.RequestParser()
parser.add_argument('plate_string')


# TODO duplicate with spz_img
def create_api_response(status_code, message, data={}):
    api_metadata = {
        'status_code': str(status_code),
        'messages': str(message),
    }
    return {**api_metadata, **data}


def create_post_response(plate_string):
    plate = {
        'plate': plate_string,
        'coordinates': None
    }
    egv_data = {}
    egv_data['data'] = create_egv_object(plate)
    return create_api_response(
        status_code=AppResponses.SUCCESS,
        message='',
        data=egv_data)


class SPZ(Resource):
    def get(self):
        return 'SPZ resource GET'

    def post(self):
        args = parser.parse_args()
        plate_string = args['plate_string']
        return create_post_response(plate_string)
