import json
import requests
import pprint

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    payload = {'id':1, 'method': 'get_bdevs'}
    url = 'http://172.20.8.1:8000/'
    req = requests.post(url,
            data=json.dumps(payload),
            auth=('test', 'test'),
            verify=False,
            timeout=30)
    pp.pprint(req.json())

    payload = {'id':2, 'method': 'get_nvmf_transports'}
    req = requests.post(url,
            data=json.dumps(payload),
            auth=('test', 'test'),
            verify=False,
            timeout=30)
    pp.pprint(req.json())

    payload = {'id':3, 'method': 'construct_null_bdev', 'params': {
    'name': 'null0',
    'num_blocks': 40960,
    'block_size': 4096
    }
    }
    req = requests.post(url,
            data=json.dumps(payload),
            auth=('test', 'test'),
            verify=False,
            timeout=30)
    pp.pprint(req.json())


