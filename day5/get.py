import requests

url = "http://192.168.1.50:5000/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
