# Here we will learn about the json module 

# JSON - Java script object notation

import json

# json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary. It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.

data = '{"var1": "shahnawaz sayyed" , "var2": 11}'
parse = json.loads(data)   # Converted the string to parsed data
print(parse)


