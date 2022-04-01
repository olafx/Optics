'''
1D Airy pattern with vertical lines showing the zeros.
'''

import matplotlib.pyplot as plt
from scipy.special import j1, jn_zeros
from numpy import linspace, pi
import sys

if __name__ == '__main__':
    xl = float(sys.argv[1])
    x = linspace(-xl, xl, int(xl * 10**3))
    I = (2 * j1(x) / x) ** 2
    x0 = jn_zeros(1, max(1, xl // pi)) # upper limit
    plt.plot(x, I, 'k', [0, 0], [0, 1], 'k--')
    for x0_ in x0:
        if x0_ < xl:
            plt.plot([ x0_,  x0_], [0, 1], 'k--',
                     [-x0_, -x0_], [0, 1], 'k--')
    plt.xlabel(r'$k a \sin \theta$')
    plt.ylabel(r'$I$')
    plt.show()
