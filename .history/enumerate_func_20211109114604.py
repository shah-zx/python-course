# Here we will learn about enumerate function 

l1 = ["Bhindi" , "Aloo" , "burger" , "sauce"]

i = 1
for item in l1:
    if i%2 is not 0:
        print(f"Ye lo tumhari cheeze :{item}")
    i = i+1