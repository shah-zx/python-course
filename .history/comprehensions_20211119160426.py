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

# dict1 = { i:f"item{i}" for i in range(100) if i%3 == 0}
# print(dict1)

# This will print the numbers from 0 to 100 multiplied by 2

# dict1 = { i*2:f"item{i}" for i in range(100)}
# print(dict1)

# Reversing the key value pairs :

# dict2 = {value:key for key, value in dict1.items()}
# print(dict2)


# Practice :

# list = []

# l = [i for i in range(0,21)]
# print(l)

# m  = [i for i in range(0 , 31) if  i % 2 == 0]
# print(m)

# Set comprehension :

dresses = {dress for dress in ["dress1"  , "dress2" , "dress3" , "dress1" , "dress2" , "dress3"] }
# print(dresses)

print(type(dresses))

# Generator comprehension : 

evens = (i for i in range(100) if i % 2 == 0)
print(evens)
