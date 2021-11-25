# Here we will learn about the json module 

# JSON - Java script object notation

import json

data = '{"var1": "shahnawaz sayyed" , "var2": 11}'
parse = json.loads(data)

print(parse)