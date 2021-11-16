# Here we will leran about the diamond shaped problem , which says that , which class will use which method :

# python and c++ supports , multiple inheritance but java doesnt.

class A:
    def met(self):
        print("This is a methid from class A")
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass


a = A()
b = B()
c = C()
d = D()
