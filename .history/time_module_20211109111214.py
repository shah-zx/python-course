# Here we will learn about the time module 

import time  # Imported the time module 

initial = time.time()
k = 0
while (k<45):
    print("Hello there : "  , k)
    k = k+1
print("While loop ran in " , time.time()-initial , "seconds")
