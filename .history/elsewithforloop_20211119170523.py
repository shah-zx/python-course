# Here we will see how can wee use for loop with else :
Khana = ["sabji" , "roti" , "daal" , "chawal" , "papad" , "achar" , "raita"]

# This is the one process that will print the items of the khana list 
for item in Khana:
    print(item)
    
    
# if we want to stop the process we can use else :

for item in Khana:
    if item == "burger":
        print("found")
else:
    print("item not found :(")    
    