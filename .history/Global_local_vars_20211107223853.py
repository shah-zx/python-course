l = 9  # This is a global variable 
def func(s):
    h = 2  # A local variable
    print(h)
    f = 7  # A local variable
    print(l)
    return s


print(l)