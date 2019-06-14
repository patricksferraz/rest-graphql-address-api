import requests

URL = "http://127.0.0.1:5000"

headers = {"content-type": "application/json"}

payload = {
    "root": """
        query {
            getState(place:"45607336") {
                id
                name
                acronym
                cities {
                    id
                    idState
                    name
                    places {
                        cep
                        idState
                        idCity
                        district
                        publicPlace
                    }
                }
            }
        }
    """
}

# root = requests.get(URL, headers=headers)
root = requests.post(
    f"{URL}/graphql", headers=headers, json={"query": payload["root"]}
)
print(root.json())
