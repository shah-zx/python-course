# Here we will make a mini project :

# Requirements :
# method for : Display books
# method for : lend book 
# method for : add book
# method for : return book 

class Library:
    def __init__(self , listofbooks , library_name):
        self.listofbooks = "alistofbooks"
        self.library_name = "alibrary_name"
        
    def info(self , library_name , listofbooks):
        print (f"The name of the library is : {self.library_name} and these are the number of books : {self.listofbooks}")
            
    
    
Nl = Library("National library" , "8500")
print(Nl)

    
    