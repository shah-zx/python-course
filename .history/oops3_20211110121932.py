class Employee:
    no_of_leaves = 10
    
    def print_details(self):   # A finction or method of the class
         return f"name is {self.name} and salary is {self.salary}"        
    
shahnawaz = Employee()   # Object one 
hamza = Employee() # Object two 

shahnawaz.name = "shahnawaz sayyed"
shahnawaz.position = "developer"
shahnawaz.grade = "A"


hamza.name = "hamza sayyed"
hamza.position = "tester"
hamza.grade = "A"
