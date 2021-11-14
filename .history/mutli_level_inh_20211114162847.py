# Multi - level inheritance :

class Dad:
    basketball = 1
    pass 

class Son(Dad):
    dance = 1
    def isDance(self):
        return f"Yes i dance !!{self.dance}"
        
    pass

class Grandson(Son):
    dance = 4
    def isDance(self):
        return f"Yes i dance!! very awesomely {self.dance}"
    pass

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isDance())

    
    