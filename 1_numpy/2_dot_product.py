# DOT PRODUCT
print('DOT PRODUCT')

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print('Array a:', a)
print('Array b:', b)

print('Perform inner product by hand')
print('There are multiple ways of doing it, but basically looping through both the arrays')
products = [a_el*b_el for a_el, b_el in zip(a,b)]
dot = np.sum(products)
print('Scalar product of a and b is:', dot)

print('If we simply do a*b we obtain the element-wise multiplication')
print(a*b)
print('So there is a smarter way of obtaining the dot product')
print('Which is to sum the elements of the array a*b')
print(np.sum(a*b))

print('A lot of numpy functions are also instance method')
print((a*b).sum())

print('So np.sum(a*b) gives the same result of (a*b).sum() -> 32')

print('Of course in numpy a dedicated function for dot product exists: np.dot() which is also an instance method!')
print(np.dot(a,b))
print(a.dot(b))
print('So you can write np.dot(a,b) or a.dot(b), still 32')

print('You can also write a@b')
print(a@b)

print('Alternative definition of scalar product')
print('||a||*||b||*cos(w)')

amag = np.sqrt(np.sum(a**2))
bmag = np.sqrt(np.sum(b**2))

print('||a||=', amag)
print('||b||=', bmag)

print('Can calculate magnitude of a with np.sqrt(np.sum(a**2)) or np.sqrt((a*a).sum()) or even np.sqrt(a.dot(a))')
#print(np.sqrt(a.dot(a)))
print('Since a dot a = ||a||**2')

print('But numpy has a dedicated module for linear algebra: linalg')
print('So we can use it for finding the magnitude of a vector')
print('||a||=', np.linalg.norm(a))
print('||b||=', np.linalg.norm(b))

print('Let us now find the cosine of the angle between a and b')
print('cos(w) = a.b / ||a||*||b||')
cosangle = a.dot(b)/(amag*bmag)
print(cosangle)

print('Therefore the angle between a and b is arccos(cos(w))')
print(np.arccos(cosangle))
