import numpy as np

# a = np.array([5, 6, 9])
# print(a[0])

# # a = np.array([[5, 6, 9], [3, 4, 6], [1, 2, 3]])
# print(a.ndim)   # This is used for printing the dimensions

# print(a.itemsize);  # this will print the size of int - 4

# print(a.dtype); # this will print the data type of array elements


# print(a.dtype); # this will print the data type of the new array

# print(a.shape);

# print(a.size);

# a = np.array([[5, 6, 9], [3, 4, 6], [1, 2, 3]] ,dtype = complex)

# print(a)

b = np.zeros((3, 4))  # This will initialize the array with all zeroes in it

print(b)

c = np.ones((3, 3))  # This will initialize the array with all ones in it.

print(c)

l = range(0, 3)  # This creates a range for the given nos

print(l[0])

print(l[1])

# Making arrays using numpy

m = np.arange(0, 5)

print(m)

c = np.arange(0, 10, 2)

print(c)

d = np.linspace(0, 10, 4)

print(d)


a = np.array([[0, 4], [1, 5], [2, 6], [3, 7]])

a.reshape(2,4)

print(a)

f = a.ravel()

print(a)

print(f)

# some mathematical functions offerred by numpy :

print(a.max())

print(a.min())

print(a.sum(axis=0));  # will add the columns 

print(a.sum(axis=1));  # will add the rows

e = np.sqrt(a);

print(e);


s = np.array([[3,4] , [5,6]])

t = np.array([[7,8] , [9,10]]);

print(s + t);  # This will print the addition


