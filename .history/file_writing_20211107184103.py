f = open("shahnawaz.txt" , "rt")  # This will open the txt file and return the pointer which will help in different operations and alo provided with a specific mode 
content = f.read()  # This will read the file and put the content in the content variable 
print(content)  # Printing the content to the output

f.close()  # Closing the file  , is a good practice 

text = f.read(5) # This will read the file and put the content in the content variable



