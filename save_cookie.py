from instagram_private_api import Client

import secrets

username = secrets.username
password = secrets.password

api = Client(username, password)
pickled_cookies_str = api.cookie_jar.dump()
open("cookie.file", mode="wb+").write(pickled_cookies_str)