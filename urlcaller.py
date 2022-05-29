from datetime import datetime
import requests


def url_caller(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is ok")

