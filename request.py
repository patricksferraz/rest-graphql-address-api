import requests

URL = "http://127.0.0.1:5000"

headers = {"content-type": "application/json"}

payload = {"root": {}}

# rtransfer = requests.post(
#     f"{URL}/partner/single-account/transfer",
#     headers=headers,
#     json=payload["post-transfer"],
# )
print("{")
root = requests.get(f"{URL}", headers=headers, params=payload["root"])
print('"Balance":\n{},'.format(root.json()))

street = requests.get(f"{URL}/street", headers=headers, params=payload["root"])
print('"Street":\n{},'.format(street.json()))
print("}")
