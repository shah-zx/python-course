

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
print(type(Rohan))  # It gives the type of the object
print(id("Hello there")) # It gives the id of the string




     