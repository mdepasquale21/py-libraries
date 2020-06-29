#SPEED TEST FOR MATRIX MULTIPLICATION
print('SPEED TEST FOR MATRIX MULTIPLICATION')

import time
import numpy as np

print('np 2-D arrays vs list of lists')

t_interval = 10
print('dot products',t_interval,'times')

matrix_a = np.random.randn(100,200)
matrix_b = np.random.randn(200,300)

list_a = list(matrix_a)
list_b = list(matrix_b)
list_b_4_op = list(matrix_b.T)

result_dim = np.zeros((100,300))
result_list = list(result_dim)

def dot_product_by_hand(a,b):
    result = 0
    for e,g in zip(a,b):
        result+= e*g
    return result

def dot_product_matrix_by_hand(a, bt, result):
    for i in range(len(a)):
        for j in range(len(bt)):
            result[i][j] = dot_product_by_hand(a[i],bt[j])
    return result

def dot_product_numpy(a,b):
    return a.dot(b)

t1 = time.time()
for i in range(t_interval):
    dot_product_matrix_by_hand(list_a, list_b_4_op, result_list)
t2 = time.time()
ht = t2-t1

t3 = time.time()
for i in range(t_interval):
    dot_product_numpy(matrix_a,matrix_b)
t4 = time.time()
nt = t4-t3

print('numpy calculation is',ht/nt,'times faster than by hand calculation')

# numpy calculation is on average about 10'000 times faster than by hand list calculation!!!!!
