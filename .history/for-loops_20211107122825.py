# Here we will learn about for loops
list1 = ["Shahnawaz", "Hamza", "Jones", "Karol", "Gayatri"]
# Now we will iterate over the list
for item in list1:   # This will iterarte over and print the elments
    print(item)
    
    print("\n")

    tup = ("Geeta", "Reeta", "sumit", "gopal")
    for item in tup:
        print(item)

# Iteration of the list of lists

list2 = [["Shahnawaz" , 2],[ "Hamza" , 4], ["Jones" , 5], ["Karol" , 8], ["Gayatri" , 7]]
print(list1)

for item , lollypop in list2: # Iterating for two fields 
    print(item  , "and lollypop are :" ,  lollypop)
    
    
