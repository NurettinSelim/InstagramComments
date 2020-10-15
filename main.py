from instagram_private_api import Client
import secrets
from utils import get_media_id

username = secrets.username
password = secrets.password

# Firstly run save_cookie.py
api = Client(username, password, cookie=open("cookie.file", mode="rb").read())

post_url = "https://www.instagram.com/p/CGSpEUOlixC/"
media_id = get_media_id(post_url)
print(media_id)

comments = api.media_n_comments(media_id, n=3000)

for i in comments:
    print(f"Username:{i['user']['username']} \n{i['text']}\n--------------------------")

print(f"Comments count:{len(comments)}")
