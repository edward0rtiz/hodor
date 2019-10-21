#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup


php = 'http://158.69.76.135/level4.php'
user_agent = ("Mozilla/5.0 (Windows NT 10.0; WOW64) \
AppelWebKit/537.36 (HTML like Gecko) Chrome/77.0.3865.90 Safari/537.36")
proxy_sites = ['https://www.free-proxy-list.net/']


header = {
    "user-agent": user_agent,
    "referer": php
}
vote = {

    "id": "931",
    "holdthedoor": "Submit",
    "key": "",
}
proxy = {
    'http': '',
}


def vote(php, vote_id):
    p = requests.get(php)
    soup = Beautifulsoup(p.text, 'html.parser')
    total = list(soup.find_all('td'))
    for i in range(len(total)):
        if vote_id in str(total[i].text):
            return int(total[i + 1].text[1:])
    return 0

if __name__ == '__main__':
    counter = 0
    reverse = 0
    while counter < 98:
        s = requests.session()
        p = s.get(proxy_sites[reverse])
        reverse = 1 if reverse == 0 else 0
        soup = BeautifulSoup(p.text, 'html.parser')
        proxy_list = soup.find('tbody').find_all('tr')

        for ip in proxy_list:
            proxy['http'] = 'http://' + ip.find('td').text
            print('Trying {}'.format(proxy['http']))
            try:
                s = requests.session()
                p = s.get(php, headers=header, proxies=proxy, timeout=1)
                soup = BeautifulSoup(p.text, 'html.parser')
                hv = soup.find("form", {"method": "post"})
                hv = hv.find("input",{"type": "hidden"})
                vote["key"] = hv["value"]

                s.post(php, headers=header, proxies=proxy, data=vote, timeout=1)
                total = vote(php, vote["id"])
                if total > counter:
                    print('... success! Vote count = {}'.format(counter))
                    counter += 1
                else:
                    print('...failed.')
            except:
                print('...failed.')
