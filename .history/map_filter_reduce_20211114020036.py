# Here we will learn about the map function 

numbers = ["1","2","3","4","5","6","7"]  # A list 

# All these numbers are strings in a list 

# Now we will convert them to numbers

# numbers = list(map(int , numbers))  # This will convert the strings in the numbers list to integers

# numbers[2] = numbers[2] + 12  # Adding 12 to 3 , checking wether the string is converted to integer or not 

# print(numbers[2])
# # def sq(a):
# #     return a*a


# num = [1,2,3,4,5,6,7]
# sq = list(map(lambda x: x*x ,num))  # sq is repalced by the lambda function 

# # square = list(map(sq, num))

# print(sq)

def square(a):
    return a*a

def cube(a):
    return a*a*a

funcs = [square, cube]  # List containing all functions

# num = [1,2,3,4,5,6,7]

for i in range(5):
    val = list(map(lambda x: x(i) , funcs))  # Lambda is a function here , which provides functions
    print(val)
    
# The filter function :
# It gives a list of elements on which a function returns true

list = [1,2,3,4,5,6]

def greater(num) :
    return num > 5 

gt_then = list(filter(greater, list))   # First convert the variable into a list , then passing the function and list.
print(gt_then)

    

