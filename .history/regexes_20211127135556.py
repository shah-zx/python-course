# Here we will leran about regexes in pyhton :

# findall , search , split , sub , finditer :




part = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''

# The above given would be our samle text..


import re

patt = re.compile(r'^dummy')
# print(r"/n")   # This r is called raw and it does not let the escape sequences to escape 
# # /n is an escape sequence but by the use of r we can convert it into a normal string
# matches = patt.finditer(part)
# for match in matches:
#     print(match)

print(patt)


