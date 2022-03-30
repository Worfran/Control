import sklearn as skt
import numpy as np
import sklearn.datasets as data
import matplotlib.pyplot as plt

dx,dy=data.load_breast_cancer(return_X_y=True)

plt.figure()
plt.plot(dx,dy)
plt.show()