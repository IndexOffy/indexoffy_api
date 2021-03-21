import requests
url = "http://api.indexoffy.com/users"

payload={}
headers = {}

for item in range(100):
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
