def searcher():   # This is our coroutine and not a function 
    import time
    # Some four seconds time consuming task.
    book = "This is a book and it is being read"
    time.sleep(4)
    
    
    while true:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Your text is not in the book")
            