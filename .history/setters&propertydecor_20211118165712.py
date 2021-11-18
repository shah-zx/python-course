# Here we will learn about setters and property decoratotrs  :

# Note : Objects of Abstract class cant be made 


class Employee():
    def __init__(self , fname , lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@gmail.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
   
    def printDetails(self):
        pass
    def printEmail(self):
        pass
   
shahnawaz_sayyed = Employee("shahnawaz" , "sayyed")  # Here we have created the instances 
hamza_sayyed = Employee("Hamza", "sayyed")

print(shahnawaz_sayyed.explain())
# print(shahnawaz_sayyed.explain())
print(shahnawaz_sayyed.email())
