# Here we will leran about the diamond shaped problem , which says that , which class will use which method :

# python and c++ supports , multiple inheritance but java doesnt.

class A:
    def met(self):
        print("This is a method from class A")
    pass
class B(A):
    def met(self):
        print("This is a method from class B")
    pass
class C(A):
    print("This is a method from class C")
    pass
class D(B,C):
    pass


a = A()
b = B()
c = C()
d = D()

d.met()
