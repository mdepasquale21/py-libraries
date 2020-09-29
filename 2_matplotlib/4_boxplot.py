# BOXPLOT
print('BOXPLOT')

import numpy as np
import matplotlib.pyplot as plt

#import matplotlib
#matplotlib.rcParams.update({'font.size':6})

names = ['Model 1', 'Model 2', 'Model 3']

values = {
          names[0]:0.13*np.random.random((10))+0.87,
          names[1]:0.07*np.random.random((10))+0.93,
          names[2]:0.10*np.random.random((10))+0.90
          }

plt.title('Accuracy')
plt.boxplot([values[model] for model in names], labels=names, showmeans=True)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('boxplot.png', dpi=250)
plt.clf()
plt.close()
