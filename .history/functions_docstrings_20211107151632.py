# Here we will learn about funtion

a = 9
b = 10
c = sum((a,b))
print(c)


# User defined functions  

def func():
    print("Hello you are in func")
    
print(func())
func()

def func2(a,b):
    avg = (a +b)/2
    return avg
    
    
v = func2(2,7)  # If we used this without the return statement , then it would have given us none 
print(v)

    
    
