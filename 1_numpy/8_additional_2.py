#SPEED TEST FOR MATRIX MULTIPLICATION
print('SPEED TEST FOR MATRIX MULTIPLICATION')

print('np 2-D arrays vs list of lists')

t_interval = 100000
print('dot products',t_interval,'times')

matrix_a = np.random.randn(100,200)
matrix_b = np.random.randn(200,300)

list_a = []
list_b = []

def dot_product_by_hand(a,b):
    result = 0
    for e,g in zip(a,b):
        result+= e*g
    return result

def dot_product_numpy(a,b):
    return a.dot(b)

t1 = time.time()
for i in range(t_interval):
    dot_product_by_hand(a,b)
t2 = time.time()
ht = t2-t1

t3 = time.time()
for i in range(t_interval):
    dot_product_numpy(matrix_a,matrix_b)
t4 = time.time()
nt = t4-t3

print('numpy calculation is',ht/nt,'times faster than by hand calculation')
