from scipy.stats import norminvgauss
import matplotlib.pyplot as plt
import numpy as np

def plot_normal(sizes : list, x_label : str, y_label : str, clr : str):
    for size in sizes:
        rv = norminvgauss(1, 0)
        histogram = norminvgauss.rvs(1, 0, size = size)

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