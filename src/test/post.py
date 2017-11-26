import base64

import requests

url = 'http://127.0.0.1'
port = 8765

with open("/tmp/ea7the.jpg", "rb") as image_file:
# with open("/home/michal/Downloads/openalpr.conf", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

res = requests.post(url="{}:{}/spz_img/".format(url, port),
                    data={
                        'image': encoded_string
                    },
                    headers={},
                    files={},
                    cookies=None,
                    auth=None)

print(res.text)
