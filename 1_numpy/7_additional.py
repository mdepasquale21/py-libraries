#SPEED TEST FOR MATRIX MULTIPLICATION
print('SPEED TEST FOR MATRIX MULTIPLICATION')

import time
import numpy as np
import matplotlib.pyplot as plt

print('How does time increase with input size?')

dimensions = [10, 100, 500, 1000, 2000, 4000, 6000, 8000, 10000, 12000]
print(dimensions)

squared_matrices_a = [np.random.randn(d,d) for d in dimensions]
squared_matrices_b = [np.random.randn(d,d) for d in dimensions]

print([mat.shape for mat in squared_matrices_a])
print([mat.shape for mat in squared_matrices_b])

times = []

t0 = time.time()
for a, b in zip(squared_matrices_a, squared_matrices_b):
    res = a@b
    t = time.time()
    times.append(t-t0)

plt.xlabel('Dimensions of square matrices')
plt.ylabel('Time (s)')
plt.title('Computation time of dot product vs dimensions of input matrices')
plt.scatter(dimensions, times, c='red')
plt.plot(dimensions, times, c='black')
#plt.legend(('data',),loc='upper right', bbox_to_anchor=(1.05, 1.15))
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.savefig('./dim_vs_time.png', dpi = 250)
plt.clf()
