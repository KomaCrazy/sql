import requests
import time
import json
url = "http://192.168.1.50:5000/2"

payload={}
headers = {}

def s1():
    time.sleep(0.5)


while True :
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text
    data = json.loads(data)
    for row in data :
        print(row)
    print("_____________________________")
    s1()
