# Here we will learn about string formatting 

me = "Harry"
a1 = 3
# a = "this %s is %s"%(me , a1)   # Thorugh the help of this we can print the variables with the string 
a = "This is {} {}"
b = a.format(me,a1)
print(b)
