# Here we will learn arguments in pyhton :
# def function_name(a,b,c,d):
#     print(a,b,c,d)


# function_name("shahnawaz" , "hamza" , "Rahul" , "Ronit")


# This is not perfect for scalable applications

# Note : first -> Normal arguments then -> args then -> kwargs

def funargs(normal, *args, **kwargs):  # When the arguments go here , then they transform into tuple
    # print(type(args))
    # print(args[0])
    print(normal)
    for item in args:
        print(item)
        print("Now i would like to introduce some of our heroes")
        for key, value in kwargs.items():
            print(f"{key, value}")

# function_name("shahnawaz" , "hamza" , "Rahul" , "Ronit")


# We will pass these items in the list to our function
har = ["shahnawaz", "hamza", "Rahul", "Ronit", "seema", "reeta", "kusum"]   
# This will also be passed as an argument in the function
normal = "This is a normal argument"
kw = {"Maths": "suwarna", "English": "priya",    # This is a dictionary , wich will go in kwargs 
      "biology": "bhagyashree", "Hindi": "bala" , "shivam" : "cook"}
funargs(normal, *har, **kw)   # Passing the list to the function



# Hello there !!!!

