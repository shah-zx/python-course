# Here we will learn about function caching :

# We save the function's input value as well as the function's output 

import time
from functools import  lru_cache  
@lru_cache(maxsize=3)   # This will save the previous three calls i.e , some_work(3)


def some_work(n):
    # some task taking some time 
    time.sleep(n)
    return n
    
    
if __name__ == '__main__':
    print("now running some work ")
    some_work(3)   # After using the lru cache , this will undergo a 3 seconds delay but after that , it will execute the next call immediately
    print("done... calling again...")
    some_work(3)
    print("Called again")