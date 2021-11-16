# Here we will leran about the diamond shaped problem , which says that , which class will use which method :

# python and c++ supports , multiple inheritance but java doesnt.

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
