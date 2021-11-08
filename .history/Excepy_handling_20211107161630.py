# print("Enter the num 1:")
# num1 = int(input())
# print("Enter the num 2:")
# num2 = int(input())
# print("The sum of two numbers is : " ,  num1 + num2)


# Now if we do something like this :

print("Enter the num 1:")
num1 = input()
print("Enter the num 2:")
num2 = input()
try:
        print("The sum of two numbers is : ",
              int(num1) + int(num2))
except Exception as e:
        print(e)
