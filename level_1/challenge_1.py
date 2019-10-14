#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

php = "http://158.69.76.135/level1.php"

vote = {
    "id": "931",
    "holdthedoor": "holdthedoor", "key": ""
}

if __name__ == "__main__":
    for i in range(0, 4096):
        s = requests.session()
        p = s.get(php)
        soup = BeautifulSoup(p.text, "html.parser")
        hv = soup.find("form", {"method": "post"})
        hv = hv.find("input", {"type": "hidden"})
        vote["key"] = hv["value"]

        s.post(php, data=vote)
