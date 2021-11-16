class rectangle:
    
    type = "rectangle" 
    sides = 4
    def __init__(self):
        self.length = 12
        self.width = 8
    
    def printArea(self):
        return f"Area is : {self.length} * {self.width}"
    
    
    