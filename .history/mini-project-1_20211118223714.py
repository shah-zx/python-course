# Here we will make a mini project :

# Requirements :
# method for : Display books
# method for : lend book 
# method for : add book
# method for : return book 

class Library:
    def __init__(self , listofbooks , library_name):
        self.alistofbooks = listofbooks
        self.alibrary_name = library_name
        
    def info(alibrary_name , alistofbooks):
        print (f"The name of the library is : {alibrary_name} and these are the number of books : {listofbooks}")
            
    
    
Nl = Library("National library" , "8500")
print(Nl.info())

    
    