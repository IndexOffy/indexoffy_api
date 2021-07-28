import requests

url = "http://api.indexoffy.com/users?email=email@indexoffy.com"

payload={}
headers = {
  'access_token': None
}

for item in range(25):
    response = requests.request("GET", url, headers=headers, data=payload)
