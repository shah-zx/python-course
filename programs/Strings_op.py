mystr = "Shahnawaz is a good boy"  # Each of the string characters is having an index 

# Slicing of the strings //

print(mystr[0:10])  # In this 0 is included but 9 is excluded 
print(len(mystr))  # Making the use of len function 
print(mystr[0:20])

# advanced slicing  or extended slicing  

print(mystr[0:10:2])  # Skipping two characters in between 0 to 10 
print(mystr[0:])  # This will take whole sring 
print(mystr[:10]) # This will take 0 to 10 automatically 
print(mystr[0:23:1])   # This and print(mystr[::]) both are same 
print(mystr[0:23:2])   # This will skip 2 characters 
print(mystr[0:23:3])   # This will skip 2 characters 
# print(mystr[23:]) # This will take the string after 23 

# Negative indexes 
# In these cases the pyhton strings serve as : 

#           -5-4-3-2-1    ... lIKE THAT 
# M O N T Y P Y T H O N
# 1234567891011... LIKE THAT.. 

print(mystr[-4:-2])   
print(mystr[::-1]) # This will make the string reverse and print it 


print((mystr.isalnum()))   # This function will check wether the given string is numeric or not 
print((mystr.isalpha()))   # This function will check wether the given string is alphabetic or not 
print(mystr.endswith("boy"))  # This will check if the string ends with boy or not 
print(mystr.count("s"))  # This will give us the total count of the character given 
print(mystr.capitalize()) # This will capitalize the string //
print(mystr.find("is")) # This will find the given string in the string 
print((mystr.lower()))   # This will change the string to lower case 
print(mystr.upper())  # Will convert the string to upper case 
print(mystr.replace("is" , "are"))  # This will replace the string with provided string 













