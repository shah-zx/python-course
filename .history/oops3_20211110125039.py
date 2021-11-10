
# # here we will learn about self and init (constructors)

# class Employee:
#     no_of_leaves = 10
    
#     def  __init__(self , aname , asalary , aposition , agrade ):    # This is the init function which helps us in making the consructor and it takes the arguments
#         self.name = aname     # Now this self will automatically change to the object of the class in which the name variable can be initialized as name
#         self.salary = asalary
#         self.position =aposition
#         self.grade =agrade
        
        
    
#     def print_details(self):   # A function or method of the class
#          return f"name is {self.name} and salary is {self.salary} and position is {self.position}"        # Self ka matlab wo object jis par ye function lagega 
    
# shahnawaz = Employee("shahnawaz" , 1200000 , "developer" , "A" )   # Object one  , in which we are passing the arguments to the constructor 
# hamza = Employee("hamza" , 1000000 , "tester" , "A") # Object two 

# # shahnawaz.name = "shahnawaz sayyed"
# # shahnawaz.position = "developer"
# # shahnawaz.grade = "A"
# # shahnawaz.salary = 1200000

# # hamza.name = "hamza sayyed"
# # hamza.position = "tester"
# # hamza.grade = "A"
# # hamza.salary = 1200000

# # print(hamza.print_details())
# # print(shahnawaz.print_details())

# # Now self is shahnawaz and all the informtaion of rohan will be printed  


# print(shahnawaz.grade)
# print((hamza.salary))

# Some practice : 



class User:
    # Giving a constructor :
    def __init__(self , username , password , email ) :
          self.name = username
          self.pwd  = password
          self.email = email
          
    def info(name , pwd , email):
        print(f"The user details are : 1) name : {name},2) password : {pwd}, 3) email : {email}")
        
        
        
shahnawaz = User("shahnawaz", "hello@12" , "sha12@gmail.com")
hamza = User("hamza", "hell@12" , "ha12@gmail.com")

print(shahnawaz.pwd)


        






