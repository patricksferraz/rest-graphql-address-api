import requests

URL = "http://127.0.0.1:5000"

headers = {"content-type": "application/json"}

# STATE
response = []
response.append(requests.get(f"{URL}/state", headers=headers))
response.append(requests.get(f"{URL}/state/Ba", headers=headers))

# CITY
response.append(requests.get(f"{URL}/state/ba/city", headers=headers))
response.append(requests.get(f"{URL}/state/ba/city/itabuna", headers=headers))

# PLACE
response.append(
    requests.get(f"{URL}/state/ba/city/itabuna/place", headers=headers)
)
response.append(
    requests.get(f"{URL}/state/ba/city/itabuna/place/45607336", headers=headers)
)

for r in response:
    print(f"{r.json()}\n\n")
