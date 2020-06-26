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

def dot_product_by_hand_list_compr(a,b):
    return np.sum([e*g for e,g in zip(a,b)])

def dot_product_numpy(a,b):
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

tl1 = time.time()
tl = dot_product_by_hand_list_compr(a,b)
tl2 = time.time()
tl_time = tl2-tl1
print('Done dot product by hand with list comprehension, result is',tl,'elapsed time:',tl_time)

print('\n')
print('numpy calculation is',h_time/n_time,'times faster than by hand calculation')
print('numpy calculation is',tl_time/n_time,'times faster than by hand calculation with list comprehension')

print('\n')
print('For more intense calculations numpy is even faster!')
t_interval = 100000
print('dot products',t_interval,'times')

th3 = time.time()
for i in range(t_interval):
    dot_product_by_hand(a,b)
th4 = time.time()
h_time2 = th4-th3

tn3 = time.time()
for i in range(t_interval):
    dot_product_numpy(a,b)
tn4 = time.time()
n_time2 = tn4-tn3

tl3 = time.time()
for i in range(t_interval):
    dot_product_by_hand_list_compr(a,b)
tl4 = time.time()
tl_time2 = tl4-tl3

print('this time numpy calculation is',h_time2/n_time2,'times faster than by hand calculation')
print('numpy calculation is also',tl_time2/n_time2,'times faster than by hand calculation with list comprehension')
