# Here we will study about the requests module :
import requests

# r = requests.get("http://api.ipstack.com/2402:8100:219d:e9e0:c592:2f2d:77b:3a83?access_key=8d297abcac507a9a10544cc1452d914c")
# print(r.text)
# print(r.status_code)

url = "http://api.ipstack.com/2402:8100:219d:e9e0:c592:2f2d:77b:3a83?access_key=8d297abcac507a9a10544cc1452d914c"
data = {
   {"ip": "2402:8100:219d:e9e0:c592:2f2d:77b:3a83", "type": "ipv6", "continent_code": "AS", "continent_name": "Asia", "country_code": "IN", "country_name": "India", "region_code": "BR", "region_name": "Bihar", "city": "Gaya", "zip": null, "latitude": 24.780000686645508, "longitude": 84.98179626464844, "location": {"geoname_id": 1271439, "capital": "New Delhi", "languages": [{"code": "hi", "name": "Hindi", "native": "\u0939\u093f\u0928\u094d\u0926\u0940"}, {"code": "en", "name": "English", "native": "English"}], "country_flag": "https://assets.ipstack.com/flags/in.svg", "country_flag_emoji": "\ud83c\uddee\ud83c\uddf3", "country_flag_emoji_unicode": "U+1F1EE U+1F1F3", "calling_code": "91", "is_eu": false}} , 
   {
       {"ip": "2402:8100:219d:e9e0:c592:2f2d:77b:3a83", "type": "ipv6", "continent_code": "AS", "continent_name": "Asia", "country_code": "IN", "country_name": "India", "region_code": "BR", "region_name": "Chandigarh", "city": "Panchkula", "zip": null, "latitude": 24.780000686645508, "longitude": 84.98179626464844, "location": {"geoname_id": 1271439, "capital": "New Delhi", "languages": [{"code": "hi", "name": "Hindi", "native": "\u0939\u093f\u0928\u094d\u0926\u0940"}, {"code": "en", "name": "English", "native": "English"}], "country_flag": "https://assets.ipstack.com/flags/in.svg", "country_flag_emoji": "\ud83c\uddee\ud83c\uddf3", "country_flag_emoji_unicode": "U+1F1EE U+1F1F3", "calling_code": "91", "is_eu": false}}
   }
}

r2 = requests.post(url = url, data = data)
print(r2)