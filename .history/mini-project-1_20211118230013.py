# Here we will make a mini project :

# Requirements :
# method for : Display books
# method for : lend book
# method for : add book
# method for : return book


print("welcome to our library management system !!")
print("--------------------******--------------------")

class Library:
    def __init__(self, listofbooks, library_name):
        self.alistofbooks = listofbooks
        self.alibrary_name = library_name

    def info(alibrary_name, alistofbooks):
        print(f"The name of the library is : {alibrary_name} and these are the number of books : {alistofbooks}")
        
    def display_books():
        pass    


# Nl = Library("eight thousand" , "National Library")
# print(Nl.alistofbooks)
# print(Nl.alibrary_name)

