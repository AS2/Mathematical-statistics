from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

def plot_poisson(mu : float, sizes : list, x_label : str, y_label : str, clr : str):
    for size in sizes:
        histogram = poisson.rvs(mu, size = size)
        rv = poisson(mu)

        fig, ax = plt.subplots(1, 1)
        ax.hist(histogram, density=True, histtype='stepfilled', color=clr, alpha = 0.55)

        x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
        ax.plot(x, rv.pmf(x), 'k--', lw=1.5)
        
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title("SIZE: " + str(size))
        plt.grid()
        plt.show()
    return