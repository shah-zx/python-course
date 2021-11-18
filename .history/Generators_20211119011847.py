# Here we will learn about generators :
# Firstly three things are there :

"""
1) Iterable - Its a python object which has these methods : __iter__() or __getitem__()
2) Iterator - Its a python object in which this function is defined : __next__()
3) Iteration - 

"""

# Generators are a type of iterators :

# for i in range (78):  # This code will generate the values from 1 to 78 at run time only 
#     print(i)
    
# Here comes our generator : 
    
def gen(n):
    for i in range(n):
        yield i
        
g = gen(3)        

# print(g.__next__())  # The generator will create an object 
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(g)
    
h = "harry"

# This below code is iterable :
for char in h:
    print(char)
    

