# Here we will learn about else and finally in try except 

f1 = open("shahnawaz.txt")
try : 
    f = open("dose.txt")
    
except Exception as e :
    print(e)

else:
    print("This will run only if the except is not  running")    
    
finally :
    print("Run this anyway")  # This is user for code clean up and will always execute 
    f1.close()
    
    
print("stuff")


# If except does not run then else will run 
