import requests

URL = "http://127.0.0.1:5000"

headers = {"content-type": "application/json"}

payload = {"root": {}}

# root = requests.post(f"{URL}/state", headers=headers, json=payload["root"])
root = requests.get(f"{URL}/state/Ba", headers=headers, params=payload["root"])
print(root.json())
