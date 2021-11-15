# Public , protected and private variables 


class Employee:
    no_of_leaves = 10
    _protec = 12
    __private = 90
    
    def  __init__(self , aname , asalary , aposition , agrade ):  # This is the init function which helps us in making the consructor and it takes the arguments
        self.name = aname     # Now this self will automatically change to the object of the class in which the name variable can be initialized as name
        self.salary = asalary
        self.position =aposition
        self.grade =agrade
        
        
class Programmer(Employee) :
    # no_of_games = 6
    def printprog(self):
        return f"The name is : {self.name}. The salary is : {self.salary}. The position is : {self.position}. The grade is : {self.grade}"
    

emp = Employee("shahnawaz",1200000 , "Devops engineer" ,"A")

print(emp._protec)  # This is a protected variable 
# We cannot access the private variable 
print(emp._Employee__private) # This is a private variable


