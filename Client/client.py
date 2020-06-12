import socket
import requests, json

url = "http://127.0.0.1:8080"

params = {"/" : "hi"}
headers = {'Hello': 'Basic HTTP!'}

res = requests.get(url, data=json.dumps(headers) ,params=params)
if 200 == res.status_code:
    print("HTTP/1.0 200 OK")
for i in res.headers:
    print(i +": "+ res.headers[i])
