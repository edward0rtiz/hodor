#!/usr/bin/python3

import requests

php = "http://158.69.76.135/level0.php"

vote = {
    "id": "931",
    "holdthedoor": "Submit"
}

if __name__ == "__main__":
    for i in range(0, 1024):
        requests.post(php, data=vote)
