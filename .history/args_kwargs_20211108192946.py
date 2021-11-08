# Here we will learn arguments in pyhton :
# def function_name(a,b,c,d):
#     print(a,b,c,d)
    

# function_name("shahnawaz" , "hamza" , "Rahul" , "Ronit")


# This is not perfect for scalable applications 

def funargs(*args):  # When the arguments go here , then they transform into tuple
    # print(type(args))
    # print(args[0])
    for item in args:
        print(item)    

# function_name("shahnawaz" , "hamza" , "Rahul" , "Ronit")

har = ["shahnawaz" , "hamza" , "Rahul" , "Ronit" , "seema" , "reeta" , "kusum"]   # We will pass these items in the list to our function 
funargs(*har)   # Passing the list to the function 
