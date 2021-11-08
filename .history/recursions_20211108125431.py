# def print2(str1):
#     # print2(str1)  # This will call itself recursively and finally will throw error of limit exceeded 
#     print("This is " + str1)
    
# print2("shahnawaz")

# Taking the example of factorial :

# Logic : n! * (n-1)!

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac


number = int(input("Enter the number :"))
print(factorial_iterative(number))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    

