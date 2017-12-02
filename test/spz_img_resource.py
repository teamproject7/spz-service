import base64
import requests

url = "{}:{}/spz_img/".format('http://127.0.0.1', '8765')
# url = "{}:{}/spz_img/".format('http://108.61.179.124', '80')


file_not_allowed = "file.txt"
file_should_recognize = "us_plate.jpg"
file_no_plate = "opencv.jpg"


def test_get():
    res = requests.get(url)
    assert res.status_code == 200, 'SPZ_IMG resource GET method is not available'


def test_post_recognize():
    res = do_post(file_should_recognize)
    res_data = res.json()
    assert res.status_code == 200 and res_data['status_code'] == 'LICENCE_PLATE_FOUND', \
        'SPZ_IMG resource POST method is not working properly'


def test_post_no_plate():
    res = do_post(file_no_plate)
    res_data = res.json()
    assert res.status_code == 200 and res_data['status_code'] == 'NO_LICENCE_PLATE_FOUND', \
        'SPZ_IMG resource POST method is not working properly'


def test_post_not_allowed():
    res = do_post(file_not_allowed)
    res_data = res.json()
    assert res.status_code == 200 and res_data['status_code'] == 'FILE_NOT_ALLOWED', \
        'SPZ_IMG resource POST method is not working properly'


def do_post(file):
    with open(file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    res = requests.post(
        url=url,
        data={'image': encoded_string},
        headers={},
        files={},
        cookies=None,
        auth=None
    )

    return res
