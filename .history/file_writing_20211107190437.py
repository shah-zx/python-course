f = open("shahnawaz.txt" , "rt")  # This will open the txt file and return the pointer which will help in different operations and alo provided with a specific mode 
# content = f.read()  # This will read the file and put the content in the content variable 
# print("3" , content)  # Printing the content to the output

# for line in content:
#     print(line) # Print the characters individually
    
    
# for line in f:  # Initially it will not give the lines because content has already read the file 
#     print(line , end="") # Print the line individually not the characters 


print(f.readline())   # This will print one line only.

f.close()  # Closing the file  , is a good practice 

# text = f.read(5) # This will read the file and put the content will upto 5 characters only 



