# Here we will learn about the labda or anonymous fucntions 

# A lambda function :

# minus = lambda x , y  : x + y

# print(minus(7,3))

# Same as : 

# def minus(x, y):
#     return x - y


def a_first(a):
    
    return a[1]

a = [[1,14] , [5,6] , [8,23]]  # This is our list of lists 

a.sort(key = a_first) #

print(a)
