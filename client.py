import json
import requests
import pprint

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    payload = {'id':1, 'method': 'get_bdevs'}
    url = 'http://172.20.8.1:8000/'
    req = requests.post(url,
            data=json.dumps(payload),
            auth=('user', 'password'),
            verify=False,
            timeout=30)
    pp.pprint(req.json())

