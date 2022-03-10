from scipy.stats import norminvgauss
import matplotlib.pyplot as plt
import numpy as np

import utils as u

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
        #plt.show()
        plt.savefig(u.SAVE_PATH + "normal"+str(size)+".png")
    return

def print_table_normal(sizes : list, repeats : int):
    for size in sizes:
        means, meds, zRs, zQs, zTRs = [], [], [], [], []
        table = [means, meds, zRs, zQs, zTRs]
        E, D = [], []
        for i in range(repeats):
            distr = norminvgauss.rvs(1, 0, size = size)
            distr.sort()
            means.append(u.mean(distr))
            meds.append(u.median(distr))
            zRs.append(u.zR(distr))
            zQs.append(u.zQ(distr))
            zTRs.append(u.zTR(distr))
        for column in table:
            E.append(round(u.mean(column), u.ROUND_SIGNS))
            D.append(round(u.dispersion(column), u.ROUND_SIGNS))
        #print("size: " + str(size))
        print(E)
        print(D)
    return