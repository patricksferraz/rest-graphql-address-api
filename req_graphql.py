import requests

URL = "http://127.0.0.1:5000/graphql"

headers = {"content-type": "application/json"}

payload = {
    "root": """
        query {
            name
            version
        }
    """
}

root = requests.post(URL, headers=headers, json={"query": payload["root"]})
print(root.json())
