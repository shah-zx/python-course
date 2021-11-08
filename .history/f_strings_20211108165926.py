# Here we will learn about string formatting 

me = "Harry"
a1 = 3
# # a = "this %s is %s"%(me , a1)   # Thorugh the help of this we can print the variables with the string 
# a = "This is {1} {0}"  # This is another way of string formatting in which we can specify the indexdes also 
# b = a.format(me,a1)
# print(b)


# Now f strings = 
a = f"this is {me} {a1}"   # the f in front of  the string will add the variables in the curly brackets to the strings          
print(a)  
b = f"This is the mutliplication of the numbers : 4 and 5 : {4*5}"
