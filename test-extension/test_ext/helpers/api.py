import requests
from pprint import pprint


def get_fact():
    resp = requests.get("https://catfact.ninja/fact")
    # print(resp.status_code)
    # print(resp.text)
    print(f"{resp.status_code}: {resp.text}")


if __name__ == '__main__':
    get_fact()
