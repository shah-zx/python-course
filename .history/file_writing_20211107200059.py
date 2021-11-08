# f = open("shahnawaz.txt" , "a")  # This will write the contetnt given to the file   
# # g = f.read() # This will read the file\
# h = f.write("Writing in the file")
# print(h)
# # print(g)
# f.close()  

# Doing a in the last will append at the last of the open 
# Doing r will read the file 
# Doing w write read the file 
# If we take a as operation and write something to the file then it will give the length of the text written to the file 


# Handle read and write both :


f = open("shahnawaz.txt" , "r+")  # This will write the contetnt given to the file   
g = f.read() # This will read the file\
# h = f.write("Writing in the file")
print(g)
# print(g)
f.close()  
