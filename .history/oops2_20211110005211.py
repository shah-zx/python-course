class Employee:
    salary = 1200000  # This is a class variable and it is the class's own property , it cant be changed
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
print(hamza.salary)   # salary will act as a variable that is created itself for the use 

print(hamza.__dict__)

