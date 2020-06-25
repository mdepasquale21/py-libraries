
# ARRAY vs LIST
print('ARRAY vs LIST')

import numpy as np

L = [1,2,3]

A = np.array([1,2,3])

print('Elements in list:')
for e in L:
    print(e)

print('Elements in numpy array:')
for e in A:
    print(e)

print('Append element to list with .append() method -> list.append(e) only for lists!!')
L.append(4)
print('List:',L)

print('Lists are mutable, numpy arrays are immutable!')

print('Append another element to same list with concatenation -> list+[e]')
print('List + [5]:', L+[5])

print('In a numpy array concatenation as in lists technically does not work')
print('What happens is BROADCASTING instead -> a+[e] adds e to each element of a')
print('With another np array')
print('np array + np array([4]):', A+np.array([4]),'-->',type(A+np.array([4])))
print('With a list')
print('np array + [4]:', A+[4],'------>',type(A+[4]))

print('Vector addition of 2 numpy arrays 1,2,3 and 4,5,6')
print(A+np.array([4,5,6]),'-->', type(A+np.array([4,5,6])))
print('Vector addition of numpy array 1,2,3 and list 4,5,6')
print(A+[4,5,6],'-->',type(A+[4,5,6]))
print('Vector addition of 2 numpy arrays of different dimensions 1,2,3 and 4,5 gives a ValueError:')
print('(the same happens when adding a numpy array 1,2,3 with a list 4,5)')
print('operands could not be broadcast together with shapes (3,) (2,)')
#print(A+np.array([4,5]))
#print(A+[4,5])
print('With 2 lists is simply concatenation')
print('[1,2,3]+[4,5]:',[1,2,3]+[4,5])

print('Scalar times numpy array')
print('2 * np array 1,2,3 : -->', 2*A)

print('Scalar times list')
print('2 * [1,2,3,4] : -->', 2*L)

print('For arrays * is multiplication, for lists * is repetition')
print('For lists is basically a different way to concatenate multiple times')
print('list*2 is the same as list+list', L*2 == L+L)

print('If you can\'t use numpy for some reason or you don\'t want to')
print('then how to perform vector operations on lists? With FOR loops!')

L2 = []

for e in L:
    L2.append(e+3)

print('Add 3 to each element of list [1,2,3,4] with a for loop')
print('New list:',L2)

print('You can do this also with LIST COMPREHENSION')
L3 = [e+3 for e in L]
print('Same result as before:',L3)

print('If I want to square all the elements of a list? list**2 gives a TypeError (unsupported operand type)')
#print(L**2)
print('Again, can do the operation with a for loop or with list comprehension')
print('[1,2,3,4] squared:', [e**2 for e in L])

print('Of course with numpy array is a lot easier')
print('np array 1,2,3 squared is simply a**2 with a the array')
print(A**2)

print('Most operators or functions act ELEMENT-WISE on numpy arrays')
print('E.g. square root of np array 1,2,3')
print(np.sqrt(A))
print('E.g. log of np array 1,2,3')
print(np.log(A))
print('E.g. exp of np array 1,2,3')
print(np.exp(A))
print('E.g. tanh of np array 1,2,3')
print(np.tanh(A))

print('Lists look like arrays (they store a bunch of elements)')
print('but they work more as a generic data structure')
print('On the contrary numpy arrays exist specifically to do math!')
