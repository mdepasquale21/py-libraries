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

print('Example of learning curve with errors')
train_sizes = np.array([50, 100, 150, 200, 250, 300, 350, 400])
train_scores_mean = np.array([1.0, 0.98, 0.96, 0.94, 0.93, 0.92, 0.91, 0.90])
train_scores_std = np.array([0.12, 0.13, 0.11, 0.10, 0.08, 0.07, 0.05, 0.03])
test_scores_mean = np.array([0.70, 0.75, 0.80, 0.82, 0.85, 0.87, 0.89, 0.90])
test_scores_std = np.array([0.14, 0.134, 0.12, 0.11, 0.09, 0.07, 0.06, 0.04])

plt.title("Learning curve")
plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training Accuracy")
plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="RSKF CV Accuracy")
plt.legend(loc="best")
plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                 train_scores_mean + train_scores_std, alpha=0.1, color="r")
plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                 test_scores_mean + test_scores_std, alpha=0.1, color="g")
plt.ylabel('Accuracy')
plt.xlabel("Training Set Size (# examples)")
plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
plt.savefig('accuracy_learning_curve.png', dpi=250)
plt.clf()
plt.close()
