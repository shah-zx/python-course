# Here we will learn about the time module 
 
# Finding out the execution time of a loop

import time  # Imported the time module 

# initial = time.time() # counting the initial time 
# k = 0
# while (k<45):
#     print("Hello there : "  , k)
#     k = k+1
# print("While loop ran in " , time.time()-initial , "seconds")



# Checking for for loop 
initial2 = time.time()   # Timing at this time 
for i in range(45):
    print("Hello there : " , i)
print("For loop ran in : " , {time.time()-initial2} , "seconds")


# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

a = time.localtime()
print(a)
