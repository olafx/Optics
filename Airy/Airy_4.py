'''
2D Airy pattern of multiple variable intensity objects.
'''

import matplotlib.pyplot as plt
import matplotlib.colors as clrs
from scipy.special import j1, jn_zeros
from numpy import random, linspace, meshgrid, zeros, max, pi, sqrt, sin, cos, log
import numpy as np

xl = 20
xl_dev = 5
n = 10

res = 1000
scale_power = .5

pos = np.random.normal(0, xl_dev, (n, 2))
I0 = np.random.exponential(1, n)
Imax = np.max(I0)

x = np.linspace(-xl, xl, res)
x, y = np.meshgrid(x, x)
d = jn_zeros(1, 1)[0]
I = np.zeros([res, res])
for i in range(n):
    x_ = np.sqrt((x - pos[i][0]) ** 2 + (y - pos[i][1])**2)
    I += I0[i] / Imax * (2 * j1(x_) / x_) ** 2
img = plt.imshow(I, extent=(-xl, xl, -xl, xl), norm=clrs.PowerNorm(scale_power), cmap='Greys_r')
plt.xlim(-xl, xl)
plt.ylim(-xl, xl)
plt.colorbar(img, label='$I / I_{max}$')
plt.show()
