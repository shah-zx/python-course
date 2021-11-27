# Here we will study about the is and ==

# == value equality - Two objects have the same value
# is = reference equality  -  Two refrences refer to the same object 

a = [2,3,4]
b = a
print(b==a)

c = a[:]
print(c==a)

print(b==c)
print(c is b)  # This will return false as b and c are to different objects 



