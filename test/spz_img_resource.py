import base64
import requests

url = "{}:{}/spz_img/".format('http://127.0.0.1', '8765')


def test_get():
    res = requests.get(url)
    assert res.status_code == 200, 'SPZ_IMG resource GET method is not available'


def test_post():
    with open("SPZ.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    res = requests.post(
        url=url,
        data={'image': encoded_string},
        headers={},
        files={},
        cookies=None,
        auth=None
    )

    assert res.status_code == 200, 'SPZ_IMG resource POST method is not available'
