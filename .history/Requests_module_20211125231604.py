# Here we will study about the requests module :
import requests

r = requests.get("https://site.financialmodelingprep.com/developer/docs")
print(r.text)
