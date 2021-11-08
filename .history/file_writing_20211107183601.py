f = open("shahnawaz.txt")  # This will open the txt file and return the pointer which will help in different operations
content = f.read()  # This will read the file and put the content in the content variable 
print(content)  # Printing the content to the output

f.close()  # Closing the file  , is a good practice 
