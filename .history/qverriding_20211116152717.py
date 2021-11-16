class A:
    classvar1 = "I am in class variable in class A"
    def __init__(self):
        self.var1 = "I am in class A's constructor "

class B(A) :
    classvar2 = "I am in class B"
    
a = A()
b = B()

print(b.classvar2)

