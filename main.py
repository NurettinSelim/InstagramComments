from instagram_private_api import Client

import secrets

username = secrets.username
password = secrets.password

# Firstly run save_cookie.py
api = Client(username, password, cookie=open("cookie.file", mode="rb").read())

"""
The post is: https://www.instagram.com/p/CGSpEUOlixC/
Its media_id is =2419176566355799106_1067259270,
Find in this link
https://api.instagram.com/oembed/?callback=&url=https://www.instagram.com/p/CGSpEUOlixC/
"""

media = api.media_n_comments("2419176566355799106_1067259270", n=3000)
comment_list = list()

for i in media:
    print(f"Username:{i['user']['username']} \n{i['text']}\n--------------------------")

print(len(media))
