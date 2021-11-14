# Multi - level inheritance :

# class Dad:
#     basketball = 1
#     pass 

# class Son(Dad):
#     dance = 1
#     def isDance(self):
#         return f"Yes i dance !!{self.dance}"
        
#     pass

# class Grandson(Son):
#     dance = 4
#     def isDance(self):
#         return f"Yes i dance!! very awesomely {self.dance}"
#     pass

# darry = Dad()
# larry = Son()
# harry = Grandson()

# print(harry.isDance())
# print(harry.basketball)  
# As the grandson is inherting the son and son is inheriting dad , then the basketball attribute will return 1

    
# Practice : 

class Tree:
    def intro():
        return f"Hello there  , i am an apple tree"
    pass

class Branch(Tree):
    pass

class Fruit(Branch):
    color = "red"
    
        