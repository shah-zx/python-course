# Here we will study about the requests module :
import requests

r = requests.get("http://api.ipstack.com/2402:8100:219d:e9e0:c592:2f2d:77b:3a83?access_key=8d297abcac507a9a10544cc1452d914c")
print(r.text)

url = "www.something.com"
data = {
    "p1" : 1 ,
    "p2" : 2 ,
}

r2 = requests.post(url = url, data = data)