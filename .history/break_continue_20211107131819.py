# Here we will learn about braek and continue statements
i = 0

while(i < 45):
    print(i)
    if(i == 44):
        break  # Stop the loop and come out
    i = i + 1

# Note : There are two kinds of while loop whoch go on and on :

# while(True):
#     print("Hello")

    # while(1):
    #     print("Hello")

    # while(True):
    #     if i+1 <=5:
    #         i =i+1
    #         continue
    #     print(i+1 , end =" ")
    #     if(i==44) :
    #         break # Stop the loop
    #     i = i+1
    #

a = 26
while(a < 45):
    if(a == 30):
        continue
    a = a+1
    print(a)
    a = a+1
