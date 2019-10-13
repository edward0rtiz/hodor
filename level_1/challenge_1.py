#!/usr/bin/python3

import requests

php = "http://158.69.76.135/level1.php"

vote = {
    "id": "931",
    "holdthedoor": "Submit"
}

if __name__ == "__main__":
    for i in range(0, 4096):
        requests.post(php, data=vote)
