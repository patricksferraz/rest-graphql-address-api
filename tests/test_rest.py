import requests

URL = "http://127.0.0.1:5000"

headers = {"content-type": "application/json"}

payload = {"root": {}}

# rtransfer = requests.post(
#     f"{URL}/partner/single-account/transfer",
#     headers=headers,
#     json=payload["post-transfer"],
# )
root = requests.get(
    f"{URL}/state?limit=5&page=2", headers=headers, params=payload["root"]
)
print(root.json())
