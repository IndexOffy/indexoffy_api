import requests

url = "http://api.indexoffy.com/users/all"

payload={}
headers = {
  'access_token': '7779177864f70a4ec0f282ffcc8fd9ba'
}

for item in range(25):
    response = requests.request("GET", url, headers=headers, data=payload)
