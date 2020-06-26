# SPEED TEST
print('SPEED TEST')
print('numpy vs by hand')

import time
import numpy as np

print('Define 2 arrays a, b with 100 random components')
a = np.random.randn(100)
b = np.random.randn(100)

def dot_product_by_hand(a,b):
    result = 0
    for e,g in zip(a,b):
        result+= e*g
    return result

def dot_product_numpy(a,b):
    a = np.array(a)
    b = np.array(b)
    return a.dot(b)

th1 = time.time()
h = dot_product_by_hand(a,b)
th2 = time.time()
h_time = th2-th1
print('Done dot product by hand, result is',h,'elapsed time:',h_time)

tn1 = time.time()
n = dot_product_numpy(a,b)
tn2 = time.time()
n_time = tn2-tn1
print('Done dot product with numpy, result is',n,'elapsed time:',n_time)

print('numpy calculation is',h_time/n_time,'times faster than by hand calculations')
