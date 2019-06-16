import utils as u
import requests
import json

URL = "http://127.0.0.1:5000"
LIMIT = 20000
headers = u.HEADERS


# STATE
def req_local_scope():
    requests.get(f"{URL}/state?limit={LIMIT}", headers=headers)


# CITY
def req_border_scope():
    requests.get(f"{URL}/state/%/city?limit={LIMIT}", headers=headers)


# PLACE
def req_global_scope():
    requests.get(f"{URL}/state/%/city/%/place?limit={LIMIT}", headers=headers)


request = [
    {
        "url": f"{URL}/state?limit={LIMIT}",
        "function": req_local_scope,
        "scope": "local",
        "blockSize": "min | med | max",
    },
    {
        "url": f"{URL}/state/%/city?limit={LIMIT}",
        "function": req_border_scope,
        "scope": "border",
        "blockSize": "min | med | max",
    },
    {
        "url": f"{URL}/state/%/city/%/place?limit={LIMIT}",
        "function": req_global_scope,
        "scope": "global",
        "blockSize": "min | med | max",
    },
]

response = []
out = open("log_test_rest.out.json", "w")
for r in u._exec(request):
    response.append(r)
out.write(json.dumps(response))
