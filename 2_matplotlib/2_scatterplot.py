# SCATTERPLOT
print('SCATTERPLOT')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

print('2-D')
data2D = np.random.randn(300,2)

plt.xlabel('x')
plt.ylabel('y', rotation=0)
plt.scatter(data2D[:, 0], data2D[:, 1], color='c', marker='o', edgecolor='b')
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.savefig('scatterplot-2D.png', dpi = 250)
plt.clf()
plt.close()

print('2-D with different class labels')
data2D_classes = np.random.randn(300,2)
data2D_classes[:150,0] +=2.5
data2D_classes[:150,1] +=1.5

# create labels
labels = np.zeros(300)
labels[:150] = 1
labels[150:] = 0
classes = np.unique(labels) # basically [0,1] but like this is more general!

plt.xlabel('x')
plt.ylabel('y', rotation=0)
for i, j in enumerate(classes):
    plt.scatter(data2D_classes[labels == j, 0], data2D_classes[labels == j, 1],
                c = [matplotlib.colors.ListedColormap(('darkred', 'darkgreen'))(i)], label = j)
plt.legend(('class 0','class 1'), loc='upper right', bbox_to_anchor=(1.05, 1.15))
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.savefig('scatterplot-2D-classes.png', dpi = 250)
plt.clf()
plt.close()

print('3-D')
data3D = np.random.randn(300,3)

fig = plt.figure()
ax = Axes3D(fig, elev=10, azim=105)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.scatter(data3D[:, 0], data3D[:, 1], data3D[:, 2], color='c', marker='o', edgecolor='b')
plt.savefig('scatterplot-3D.png', dpi = 250)
plt.clf()
plt.close()
