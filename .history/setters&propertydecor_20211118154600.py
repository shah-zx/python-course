# Here we will learn about setters and property decoratotrs  :

# Note : Objects of Abstract class cant be made 


class Employee():
    def __init__(self , fname , lname):
        self.fname = fname
        self.lname = lname
        
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
   
    def printDetails(self):
        pass
   
   
shahnawaz_sayyed = Employee("shahnawaz" , "sayyed")
hamza_sayyed = Employee("Hamza", "sayyed")
