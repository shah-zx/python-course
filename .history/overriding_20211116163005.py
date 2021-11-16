# Here we will learn about overriding the operators 

class Employee:
    no_of_leaves = 4
    def __init__(self , aname , asalary , aposition , agrade):
        self.aname = aname
        self.asalary = asalary
        self.aposition = aposition
        self.agrade = agrade
        
    def printdetails(self):
        return f"The name is : {self.aname}  , salary is : {self.salary} , position is : {self.position} and the agrade is : {self.agrade}"
    
emp1 = Employee("shahnawaz" , 1200000 , "developer" , "A")
print(emp1.printdetails)


        