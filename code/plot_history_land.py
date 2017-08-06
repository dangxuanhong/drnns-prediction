import sys 
import matplotlib.pyplot as plt
import numpy as np
from utils import set_trace

dataname= sys.argv[-3]

title = sys.argv[-2]

analysis= sys.argv[-1]

# Read training log
history = np.genfromtxt(dataname, names=True, delimiter=",")

# Summarize history for MAE
plt.plot(history['mean_absolute_error'])
plt.title(title)
plt.ylabel('Mean absolute error')
plt.xlabel('Epoch')
plt.legend(['Training set'], loc='upper left')
plt.savefig('results/land-plots/mae-{}-{}'.format(dataname,analysis))