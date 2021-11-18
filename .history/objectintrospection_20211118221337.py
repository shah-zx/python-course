

# Object introspection means : to gain knowledge about any object like : its class etc..


class User:
    no_of_leaves = 12
    
    # Giving a constructor :
    def __init__(self , username , password , email ) :
          self.name = username
          self.pwd  = password
          self.email = email
          
    def info(name , pwd , email):
        print(f"The user details are : 1) name : {name},2) password : {pwd}, 3) email : {email}")
        
        # A class method :
    def change_leaves(cls , newleaves):   # This will change the no_of_leaves for the User class 
         cls.no_of_leaves = newleaves
        
    def from_str(cls , string):
         params = string.split("-")
         return cls(params[0] , params[1]) , params[2]
     
     
Rohan = User("rhn" , "Hello" , "Rh12@gmail.com")
# print(type(Rohan))  # It gives the type of the object
# print(id("Hello there")) # It gives the id of the string (The id in the memory , from which it's stored)
# o = "Hello"
# print(dir(o))



import inspect  # This is the inspect module 

# The inspect module provides several useful functions to help get information about live objects such as modules, classes, methods, functions, tracebacks, frame objects, and code objects. For example, it can help you examine the contents of a class, retrieve the source code of a method, extract and format the argument list for a function, or get all the information you need to display a detailed traceback.

# There are four main kinds of services provided by this module: type checking, getting source code, inspecting classes and functions, and examining the interpreter stack.

# print(inspect.getmembers(Rohan))

print(inspect.getmembers(User))
print(inspect.Attribute(User))


     