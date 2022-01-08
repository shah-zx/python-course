import numpy as np

a = np.array([5, 6, 9])
print(a[0])

a = np.array([[5, 6, 9], [3, 4, 6], [1, 2, 3]])
print(a.ndim)   # This is used for printing the dimensions 

print(a.itemsize);  # this will print the size of int - 4

print(a.dtype); # this will print the data type of array elements

a = np.array([[5, 6, 9], [3, 4, 6], [1, 2, 3]] ,dtype = np.float64)

print(a.dtype); # this will print the data type of the new array

print(a.shape);

print(a.size);  

a = np.array([[5, 6, 9], [3, 4, 6], [1, 2, 3]] ,dtype = complex)

print(a)

b = np.zeros((3,4))  # This will initialize the array with all zeroes in it 

print(b)

c = np.ones((3,3)) # This will initialize the array with all ones in it.






