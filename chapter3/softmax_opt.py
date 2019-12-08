import numpy as np

a = np.array([1010,1000,990])
np.exp(a) / np.sum(np.exp(a))
c = np.max(a)

a - c
np.exp(a-c) / np.sum(np.exp(a-c))

