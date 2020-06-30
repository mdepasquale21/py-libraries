# LINE CHART
print('LINE CHART')

import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams.update({'font.size':6})

print('Create fake data for x with np.linspace(min,max,n_points)')
x = np.linspace(0,20,1000)
print('Define a function for y')
y = np.sin(x) + 0.5*x

plt.xlabel('x')
plt.ylabel('y', rotation=0)
#plt.title('')
plt.plot(x,y,c='g')
#plt.legend(('data'), loc='upper right', bbox_to_anchor=(1.05, 1.15))
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig('./line_chart.png',dpi=250)
plt.clf()
plt.close()
