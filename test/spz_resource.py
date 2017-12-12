import requests

# TODO duplicate
url = "{}:{}/spz/".format('http://127.0.0.1', '8765')
# url = "{}:{}/spz_img/".format('http://108.61.179.124', '7486')


plate_exmpl = "BA-123AB"


def test_get():
    res = requests.get(url)
    assert res.status_code == 200, 'SPZ resource GET method is not available'


def test_post():
    res = do_post(plate_exmpl)
    res_data = res.json()
    assert res.status_code == 200 and res_data['status_code'] == 'SUCCESS' \
           and 'plate' in res_data['data'], \
        'SPZ_IMG resource POST method is not working properly'


def do_post(plate):
    res = requests.post(
        url=url,
        data={'plate_string': plate},
        headers={},
        files={},
        cookies=None,
        auth=None
    )

    return res
