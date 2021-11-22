# Here we will learn about function caching :
import time

def some_work(n):
    # some task taking some time 
    time.sleep(n)
    return n
    
    
if __name__ == '__main__':
    print("now running some work ")
    some_work(3)
    print("done")