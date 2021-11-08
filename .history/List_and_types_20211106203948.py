# List is a data structure

grocery = ["vimbar", "deo", "turmeric", "harpic", 67]  # This is a list
print(grocery)

# Strings items are accessible by indexes

print(grocery[0])
print(grocery[1])
print(grocery[2])
print(grocery[3])

# print(grocery[10])  This is not possible

numbers = [5, 6, 7, 8, 9]

# Accssing the numbers

print(numbers[3])
print(numbers[4])

# print(numbers[5])
# numbers.sort()  # Sorting the numbers by using the sort function
numbers.reverse() # Reverse the numbers 
print(numbers)  # This will give us the numbers  

# Slicing

print(numbers[0:5]) # This will give us the whole list and numbers[:] this is the same //
print(numbers[1:]) # This will give the list after skipping the first element as it automatically takes 5 as the 
print(numbers[2:]) # This will give the list after skipping the first element //
print(numbers[3:]) # This will give the list after skipping the first element //
print(numbers[1:3]) # This will take the number at position 1 and not the index of the last index given 

# Extended slicing 

print(numbers[::])





