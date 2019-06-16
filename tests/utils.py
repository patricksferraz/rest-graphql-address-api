from statistics import mean
import requests
import timeit

REPEAT = 100
HEADERS = {"content-type": "application/json"}


def _get(url):
    r = requests.get(url, headers=HEADERS)
    return {"size": r.headers["Content-Length"], "content": r.json()}


def _exec(operations):
    for o in operations:
        r = _get(o["url"])
        time = timeit.repeat(o["function"], repeat=REPEAT, number=1)
        yield {
            "scope": o["scope"],
            "blockSize": o["blockSize"],
            "size": r["size"],
            "time": mean(time),
        }
