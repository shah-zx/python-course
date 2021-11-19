# Here we will learn about comprehension

# If we want to print the list of numbers which are divisible by 3 then : 


# list = [3,6,9,12] # One way


# ls = []

# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)
        
# print(ls)

# We can do the same thing using comprehensions : 

# This will print all the numbers from 0 to 100 :

# This is list comprehension :

# ls = [i for i in range(100)]
# print(ls)

# This is dictionary comprehension :

# {0:"item-0" , 1:"item-1" , 2:"item-2"}

# Doing this with dictionary comprehension :

dict1 = { i*2:f"item{i}" for i in range(100)}
print(dict1)



