# Here we will learn arguments in pyhton :
# def function_name(a,b,c,d):
#     print(a,b,c,d)
    

# function_name("shahnawaz" , "hamza" , "Rahul" , "Ronit")


# This is not perfect for scalable applications 

# Note : first -> Normal arguments then -> args then -> kwargs

def funargs(normal, *args , **kwargs):  # When the arguments go here , then they transform into tuple
    # print(type(args))
    # print(args[0])
    print(normal)      
    for item in args:
        print(item)    
        for it in kwargs:
            print(it) 

# function_name("shahnawaz" , "hamza" , "Rahul" , "Ronit")

har = ["shahnawaz" , "hamza" , "Rahul" , "Ronit" , "seema" , "reeta" , "kusum"]   # We will pass these items in the list to our function 
normal = "This is a normal argument"  # This will also be passed as an argument in the function 
kw = {"Maths" : "suwarna" , "English" : "priya" , "biology" : "bhagyashree" , "Hindi" : "bala"}
funargs(normal , *har , **kw)   # Passing the list to the function 
