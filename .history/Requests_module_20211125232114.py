# Here we will study about the requests module :
import requests

r = requests.get("https://api.ipstack.com/")
print(r.text)
