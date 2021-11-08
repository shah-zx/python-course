# Here we will learn arguments in pyhton :
# def function_name(a,b,c,d):
#     print(a,b,c,d)
    

# function_name("shahnawaz" , "hamza" , "Rahul" , "Ronit")


# This is not perfect for scalable applications 

def funargs(*args):
    print(args[0])
    

function_name("shahnawaz" , "hamza" , "Rahul" , "Ronit")



har = ["shahnawaz" , "hamza" , "Rahul" , "Ronit"]
fun_args(*har)