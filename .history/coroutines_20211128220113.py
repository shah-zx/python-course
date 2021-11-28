def searcher():   # This is our coroutine and not a function 
    import time
    import packageharry
    
    
    # Some four seconds time consuming task.
    book = "This is a book and it is being read"
    time.sleep(4)
    
    
    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Your text is not in the book")
            
            
search = searcher()
print("Searching started....")
next(search)

search.send("book")
packageharry.good(10)
