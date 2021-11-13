# Here we will learn about the map function 

numbers = ["1","2","3","4","5","6","7"]  # A list 

# All these numbers are strings in a list 

# Now we will convert them to numbers


numbers = list(map(int , numbers))  # This will convert the strings in the numbers list to integers

numbers[2] + 12