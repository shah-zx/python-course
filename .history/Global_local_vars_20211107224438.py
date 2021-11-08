l = 9  # This is a global variable 
def func(s):
    h = 2  # A local variable
    print(h)
    f = 7  # A local variable
    print(l)
    return s


print(l)
func("Hello")

# Note : Initially we dont have the permission to change the global variable but if we do : Global then varoiable name , then we can change the global variable too