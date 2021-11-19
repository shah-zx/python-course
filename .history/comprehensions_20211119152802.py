# Here we will learn about comprehension

# If we want to print the list of numbers which are divisible by 3 then : 


list = [3,6,9,12] # One way


ls = []

for i in range(100):
    if i%3 == 0:
        ls.append(i)
        
print(ls)
