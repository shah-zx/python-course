class Employee:
    salary = 1200000
    pass

shahnawaz = Employee()   # Object one 
hamza = Employee() # Object two 

shahnawaz.name = "shahnawaz sayyed"
shahnawaz.position = "developer"
shahnawaz.grade = "A"


hamza.name = "hamza sayyed"
hamza.position = "tester"
hamza.grade = "A"

print(Employee.salary)