# Dictionary is nothing but key value pairs 

d1 = {}
print(type(d1))
d2 = {"Harry" : "Burger" , "Rohan" : "Fish" , "Hamza" : "Roti" , "Reeta" : {"B" : "Paratha" , "L" : "Daal" , "D" : "Pulao"}}
# Here Reeta is anotehr dictobary and it is the dictionary inside the dictionary 
print(d2["Rohan"])  # Through the help of [] we can find out the pair 
print(d2["Reeta"])  # This will print the whole dictionary 
print(d2["Reeta"]["B"])  # This will print the breakfast of reeta : d2 dictionary -> reeta dictionary -> B

# How to add another key value pair : 

d2["James"] = "Biscuit"
print(d2)
d2["Aurangzeb"] = "Kebabs"
print(d2)






