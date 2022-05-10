import requests
import json
url = "http://192.168.1.50:5000/1"

payload={}
headers = {}
i = 0



while i <= len(box) :
    response = requests.request("GET", url, headers=headers, data=payload)
    box = box.split("}")
    box = str(box[1]) + "}"
    boxlen = len(box)
    box = json.loads(box)
    print(box)
    i = i + 1
