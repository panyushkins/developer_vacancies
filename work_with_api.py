import requests


def make_superjob_request(key, method, payload):
    url = 'https://api.superjob.ru/2.0/' + method
    headers = {'X-Api-App-Id': key}
    r = requests.get(url, headers=headers, params=payload)
    return r.json()