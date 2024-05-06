#!/usr/bin/python3
"""
Get a users github id provided the username, personal access token
Uses the github api (Basic Authentication)
"""
import requests
from sys import argv


headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer {}".format(argv[2]),
        "X-Github-Api-Version": "2022-11-28"
        }
url = "https://api.github.com/users/{}".format(argv[1])
req = requests.get(url, headers=headers)
print(req.json().get("id", None))
