
import requests


def ingest_from_api(URL):
    print(URL)
    API_response = requests.get(URL)
    if API_response.status_code != 200:
        raise Exception("API call failed")
    data = API_response.json()
    print(type(data))
    return data