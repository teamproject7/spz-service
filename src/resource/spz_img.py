from flask_restful import reqparse, Resource, abort

from src.my_filestorage import save_b64_to_file, allowed_file
from src.my_openalpr import recongnize as recognize_img
from src.responses import AppResponses
from src.messages import AppMessages
from src.model.egv import generate_egv_response

parser = reqparse.RequestParser()
parser.add_argument('image')


def create_api_response(status_code, message, data={}):
    api_metadata = {
        'status_code': str(status_code),
        'messages': str(message),
    }
    return {**api_metadata, **data}


def create_post_response(data):
    if len(data['results']) > 0:

        egv_data = generate_egv_response(data)
        return create_api_response(
            status_code=AppResponses.LICENCE_PLATE_FOUND,
            message=AppMessages.LICENCE_PLATE_FOUND,
            data=egv_data
        )
    else:
        return create_api_response(
            status_code=AppResponses.NO_LICENCE_PLATE_FOUND,
            message=AppMessages.NO_LICENCE_PLATE_FOUND
        )


# TODO "DEFINE CUSTOM ERROR" http://flask-restful.readthedocs.io/en/0.3.5/extending.html
class SPZ_IMG(Resource):
    def get(self):
        return 'SPZ_IMG resource GET'

    def post(self):
        args = parser.parse_args()

        fpath = save_b64_to_file(args['image'])

        if not fpath:
            return create_api_response(
                message=AppMessages.UNEXPECTED_ERROR,
                status_code=AppResponses.UNEXPECTED_ERROR
            )

        if not allowed_file(fpath):
            return create_api_response(
                message=AppMessages.FILE_NOT_ALLOWED,
                status_code=AppResponses.FILE_NOT_ALLOWED
            )

        else:
            res = recognize_img(fpath)
            return create_post_response(res)
