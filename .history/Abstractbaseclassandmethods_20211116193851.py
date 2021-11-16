# Here we learn about Abstract classes 

# Our base class :

from abc import ABCMeta , abstractmethod

class Shape(metaclass=ABCMeta):  # This class is being inherited by ABCmeta class which gives the class the power to order the child classes to define some particular methods in them ( Here : printArea)
    @abstractmethod
    def printArea(self):
        return 0
    


class rectangle(Shape):
    
    type = "rectangle" 
    sides = 4
    def __init__(self):
        self.length = 12
        self.width = 8
    
    def printArea(self):
        return self.length * self.width
    
rect = rectangle()    
print(rect.printArea())

