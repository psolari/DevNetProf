import requests
from pprint import pprint
import json

url = "https://api.discogs.com/artists/1/releases"
i = 2

def get_pages(url):
    response = requests.get(url)
    data = response.json()
    formatted_response = json.dumps(data, indent=4)
    print(formatted_response)
    status = response.status_code
    return status, data


status, data = get_pages(url)
print("Page 1")

while status == 200:
    if "next" in data["pagination"]["urls"]:
        url = data["pagination"]["urls"]["next"]
        status, data = get_pages(url)
        print(f'Page {i}')
        i += 1
    else:
        status = "donzel"
