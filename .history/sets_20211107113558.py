# Here we will learn about sets 

s = set()  # This is an empty set 
s_from_list = set([1,2,3,4])  # This is a set having list in it 
print(type(s))
print(s_from_list)  
l = [3,4,5,6]
new_set = set(l) # This is a set where l is the list 
print(new_set) 


# Adding elements to the s set 

s.add(9)
s.add(10)
print(s)

# Union operation 

s1 = s.union({1,2,3})  # This is the set which is containing the union operation having some elements
print(s1)   
s2 = s.intersection({1,9,3}) # This is the set which is containing the intersection operation having some elements
print(s2) 
# One unique thing about set is that it contains only unique elements 
# Disjoint operation

# s3 = {8,7,6}
# print(s.disjoint(s3))




