# Here we will learn about the time module 

import time  # Imported the time module 

initial = time.time() # counting the initial time 
k = 0
while (k<45):
    print("Hello there : "  , k)
    k = k+1
print("While loop ran in " , time.time()-initial , "seconds")


for i in range(45):
    print("Hello there : " , i)
print("For loop ran in : " , {time.time()-initial} , "seconds")