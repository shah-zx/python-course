# Here we will learn about overriding the operators 

class Employee:
    no_of_leaves = 4
    def __init__(self , aname , asalary , aposition , agrade):
        self.aname = aname
        self.asalary = asalary
        self.aposition = aposition
        self.agrade = agrade
        
    def printdetails(self):
        return f"The name is : {self.aname}  , salary is : {self.asalary} , position is : {self.aposition} and the agrade is : {self.agrade}"
    def __add__(self, other):  # This is a dunder method which helps in overriding
        return self.salary + other.salary
    def __truediv__(self , other): # This is a dunder method which helps in overriding
        return self.salary / other.salary
    
emp1 = Employee("shahnawaz" , 1200000 , "developer" , "A")
emp2 = Employee("hamza" , 1000000 , "tester" , "A")
print(emp1.printdetails())

print(emp1 / emp2)
