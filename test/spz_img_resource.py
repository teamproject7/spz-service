import base64
import requests

url = "{}:{}/api/v1.0/spz_img/".format('http://127.0.0.1', '8765')
# url = "{}:{}/spz_img/".format('http://108.61.179.124', '7486')


file_should_recognize = "sk_plate.jpg"
file_should_recognize_multiple = "multiple_plates.jpg"
file_no_plate = "opencv.jpg"
file_not_allowed = "file.txt"
file_too_big = "image_too_big.jpeg"


def test_get():
    res = requests.get(url)
    assert res.status_code == 200, 'SPZ_IMG resource GET method is not available'


def test_post_recognize():
    res = do_post(file_should_recognize)
    res_data = res.json()
    assert res.status_code == 200 and res_data['status_code'] == 'SUCCESS', \
        'SPZ_IMG resource POST method is not working properly'


def test_post_recognize_multiple():
    res = do_post(file_should_recognize_multiple)
    res_data = res.json()
    found_plates_count = len(res_data['data'])
    assert res.status_code == 200 and res_data['status_code'] == 'SUCCESS' and found_plates_count >= 2, \
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


def test_post_image_size_reached():
    res = do_post(file_too_big)
    res_data = res.json()
    assert res.status_code == 200 and res_data['status_code'] == 'IMAGE_FILE_SIZE_TOO_BIG', \
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
