# Here we will study about raise :
a = input("What is your name")
b = input("How much do you earn")

if b==0:
    raise ZeroDivisionError("b is 0 so stoping the process")

if a.isnumeric():
    raise Exception("Numbers are not allowed")
print(f"Hello {a}")

# 1000 lines taking one hour 
