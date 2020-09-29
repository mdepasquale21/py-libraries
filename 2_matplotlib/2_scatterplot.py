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

print('2-D scatterplot with Decision Boundary')
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(data2D_classes, labels)
from matplotlib.colors import ListedColormap

plt.figure(figsize=(10,10))
X1, X2 = np.meshgrid(np.arange(start = data2D_classes[:, 0].min() - 1, stop = data2D_classes[:, 0].max() + 1, step = 0.01),
                     np.arange(start = data2D_classes[:, 1].min() - 1, stop = data2D_classes[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(labels)):
    plt.scatter(data2D_classes[labels == j, 0], data2D_classes[labels == j, 1],
                c = [ListedColormap(('darkred', 'darkgreen'))(i)], label = int(j))
plt.title('Decision Boundary')
plt.xlabel('X1')
plt.ylabel('X2', rotation=0)
plt.legend()
plt.savefig('scatterplot-2D-decision-boundary.png', dpi=250)
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
