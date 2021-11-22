# Here we will learn about else and finally in try except 

f1 = open("shahnawaz.txt")
try : 
    f = open("dose.txt")
    
except Exception as e :
    print(e)
    
finally :
    print("Run this anyway")
    f1.close()
    
    
print("stuff")
