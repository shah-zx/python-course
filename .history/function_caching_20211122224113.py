# Here we will learn about function caching :

# We save the function's input value as well as the function's output 


import time

def some_work(n):
    # some task taking some time 
    time.sleep(n)
    return n
    
    
if __name__ == '__main__':
    print("now running some work ")
    some_work(3)
    print("done")
    some_work(3)
    print("Called again")