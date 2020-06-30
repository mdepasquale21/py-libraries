# HISTOGRAM
print('HISTOGRAM')

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(10000)

plt.xlabel('x')
plt.ylabel('Counts', rotation=90)
plt.hist(x, bins=50)
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.savefig('histogram_normal.png',dpi=250)
plt.clf()
plt.close()

xu = np.random.random(10000)

plt.xlabel('x')
plt.ylabel('Counts', rotation=90)
plt.hist(xu, bins=50)
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.savefig('histogram_uniform.png',dpi=250)
plt.clf()
plt.close()
