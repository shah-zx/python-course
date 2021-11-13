
# Decotrators modify the functionality of a function 

# def function1 ():
#     print("This is function 1")
    
# function = function1  # Not caling the function  , but assigning the value of function to function 1

# del function1   # deleting the function1 
# function()

def funcret(num1):  # A function which returns a function
    if(num1 == 0):
        return print
    if(num1 == 1):
        return int
    
a = funcret(1)
print(a)


# Seeing the exact way : when we pass the function a function itself

def executor(func):
    func("this is printed by the print function")
    
    
executor(print)  # We gave the print fucntion in the argument and we got the msg prnted

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Harry is a good boy")
        
def who_is_harry():
    print("Harry is an instructor")


who_is_harry = dec(who_is_harry)
who_is_harry()
        