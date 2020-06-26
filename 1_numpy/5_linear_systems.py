# LINEAR SYSTEMS
print('LINEAR SYSTEMS')

import numpy as np

print('Define a simple linear system')
print('x + y = 5000')
print('3x + 7y = 10000')
b = np.array([5000, 10000])
coeff = np.array([[1,1],[3,7]])
print('Let us put it in matrix form')
print('A dot x = b')
print('coefficient matrix A')
print(coeff)
print('constant term b')
print(b)
print('unknown vector x = [x,y]')
print('The system has a solution if determinant of coefficient matrix is different from 0 (det(A)!=0)')
print('So coefficient matrix can be inverted (has an inverse A^-1)')
print('determinant', np.linalg.det(coeff))
inv_coeff = np.linalg.inv(coeff)
print('inverse matrix', inv_coeff)
print('Then the solution is x = A^-1 dot b')
print('Basically you multiply each side of the equation by A^-1 -> A^-1 dot A dot x = A^-1 dot b -> x = A^-1 dot b')
x = inv_coeff@b
print(x)
print('Let us check that this is in fact the solution with np.allclose(A@x, b)')
print(np.allclose(coeff@x, b))
