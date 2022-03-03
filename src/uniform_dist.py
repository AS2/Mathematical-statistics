from cmath import sqrt
from scipy.stats import uniform
import matplotlib.pyplot as plt
import numpy as np

def plot_uniform(begin : float, lngth : float, sizes : list, x_label : str, y_label : str, clr : str):
    for size in sizes:
        #rv = uniform(loc = begin, scale = lngth)
        #rv = uniform(loc = -sqrt(3), scale = 2 * sqrt(3))
        rv = uniform(loc = -1.7320508, scale = 2 * 1.7320508)

        #histogram = uniform.rvs(size = size, loc = begin, scale = lngth)
        histogram = uniform.rvs(size = size, loc = -sqrt(3), scale = 2 * sqrt(3))

        fig, ax = plt.subplots(1, 1)
        ax.hist(histogram, density=True, histtype='stepfilled', color=clr, alpha = 0.55)

        x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), 100)
        ax.plot(x, rv.pdf(x), 'k--', lw=1.5)
        
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title("SIZE: " + str(size))
        plt.grid()
        plt.show()
    return