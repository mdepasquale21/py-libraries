# GENERATE DATA
print('GENERATE DATA')
print('Generating data with large sizes is necessary in some cases')
print('E.g. If you need to initialize random matrices for weights and biases of a Neural Network')
print('or generate synthetic data to test a Machine Learning algorithm')

import numpy as np

print('\n')
print('Examples with numpy')
print('1) np.zeros((n_rows, n_cols)) -> MATRIX OF ALL 0s')
print('np.zeros((2,3))')
print('   |')
print('   V')
print(np.zeros((2,3)))

print('2) np.ones((n_rows, n_cols)) -> MATRIX OF ALL 1s')
print('np.ones((2,3))')
print('   |')
print('   V')
print(np.ones((2,3)))

print('3) N * np.ones((n_rows, n_cols)) -> MATRIX OF ALL Ns')
print('10 * np.ones((2,3))')
print('   |')
print('   V')
print(10*np.ones((2,3)))

print('4) n.eye(n_rows) -> DIAGONAL MATRIX')
print('np.eye(3)')
print('   |')
print('   V')
print(np.eye(3))

print('\n')
print('Array with random numbers with np.random module')
print('\n')

print('1) np.random.random() returns a random float number in the interval [0.0, 1.0) with UNIFORM distribution')
print('To draw from an interval [a, b) just do (b-a)*np.random.random()+a')
print('E.g. random number between 100 and 200')
print(100.0*np.random.random()+100.0)
print('You can pass a tuple with (n_rows, n_cols) to np.random.random() and have an array of the given shape with random numbers')
print('np.random.random((2,3)) -> 2x3 matrix between 0 and 1')
print('   |')
print('   V')
print(np.random.random((2,3)))
print('100 * np.random.random((2,3)) -> 2x3 matrix between 0 and 100')
print('   |')
print('   V')
print(100*np.random.random((2,3)))
print('100 * np.random.random((2,3)) + 100 -> 2x3 matrix between 100 and 200')
print('   |')
print('   V')
print(100*np.random.random((2,3))+100)
print('1000 * np.random.random((2,3)) - 500 -> 2x3 matrix between -500 and 500')
print('   |')
print('   V')
print(1000*np.random.random((2,3))-500)

print('\n')

print('2) If you want to draw numbers from a NORMAL distribution you should use np.random.randn()')
print('np.random.randn() draws from a GAUSSIAN distribution with mean 0 and std 1')
print('N.B. THIS TIME YOU DO NOT PASS THE TUPLE (n_rows, n_cols) BUT JUST THE TWO INTEGERS n_rows, n_cols')
print('np.random.randn(2,3)')
print('   |')
print('   V')
print(np.random.randn(2,3))

print('\n')
print('EXAMPLE 1: CREATION OF A LARGE 1-D ARRAY')
print('with 10 000 elements -> np.random.randn(10000)')
R = np.random.randn(10000)
#print(R[0:5], len(R))
print('say array is R')
print('calculate R\'s mean with np.mean(R) or R.mean()')
#print(np.mean(R))
print(R.mean())
print('calculate R\'s standard dev with np.std(R) or R.std()')
#print(np.std(R))
print(R.std())
print('calculate R\'s variance with np.var(R) or R.var()')
#print(np.var(R))
print(R.var())

print('\n')
print('EXAMPLE 2: CREATION OF A LARGE MATRIX (2-D ARRAY)')
print('with 10 000 rows and 3 columns -> np.random.randn(10000,3)')
M =  np.random.randn(10000,3)
print('say matrix is M')
print(M)
print('shape',M.shape)
print('Mean of each column (mean by rows)')
print('M.mean(axis=0)')
mean_rows = M.mean(axis=0)
print(mean_rows)
print('shape',mean_rows.shape)
print('Mean of each row (mean by columns)')
print('M.mean(axis=1)')
mean_cols = M.mean(axis=1)
print(mean_cols)
print('shape',mean_cols.shape)
