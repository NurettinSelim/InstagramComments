import json

import requests


def get_media_id(url):
    r = requests.get(f'https://api.instagram.com/oembed/?callback=&url={url}')
    json_object = json.loads(r.text)
    return json_object["media_id"]
