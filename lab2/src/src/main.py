import numpy as np
import scipy.stats as stats
import math as m

from task1 import count_coefficients, create_table, multivariate_normal, show_ellipse, mix_multivariate_normal
from task2 import reference_noisy_function, plot_linear_regression
from task3 import task3Solver
from task4 import normal, mean, dispersion_exp

# TASK 1 CODE
def task1_builder():
    sizes = [20, 60, 100]
    ros = [0, 0.5, 0.9]
    REPETITIONS = 1000

    for size in sizes:
        for ro in ros:
            pearson, spirman, quadrant = count_coefficients(multivariate_normal, size, ro, REPETITIONS)
            print('\n' + str(size) + '\n' + str(create_table(pearson, spirman, quadrant, size, ro, REPETITIONS)))

        pearson, spearman, quadrant = count_coefficients(mix_multivariate_normal, size, 0, REPETITIONS)
        print('\n' + str(size) + '\n' + str(create_table(pearson, spirman, quadrant, size, -1, REPETITIONS)))
        show_ellipse(size, ros)
    return

# TASK 2 CODE
# Without any perturbations
def task2_builder():
    x = np.arange(-1.8, 2, 0.2)
    y = reference_noisy_function(x)
    plot_linear_regression('NoPerturbations', x, y)

    # With perturbations in first and last elements
    x = np.arange(-1.8, 2, 0.2)
    y = reference_noisy_function(x)
    y[0] += 10
    y[-1] -= 10
    plot_linear_regression('Perturbations', x, y)
    return

def task3_builder():
    sizes = [20, 100]
    alpha = 0.05
    p = 1 - alpha

    # for normal ditribution
    task3Solver(sizes[1], np.random.normal(0, 1, size=sizes[1]), p, alpha)

    # for laplace ditribution
    task3Solver(sizes[0], stats.laplace.rvs(size=sizes[0], scale=1 / m.sqrt(2), loc=0), p, alpha)

    # for uniform ditribution
    task3Solver(sizes[0], stats.uniform.rvs(size=sizes[0], loc=-m.sqrt(3), scale=2 * m.sqrt(3)), p, alpha)

    return

def task4_builder():
    alpha = 0.05
    for n in [20, 100]:
        print("=========%i==========" % n)
        x = normal(n)
        m = mean(x)
        s = np.sqrt(dispersion_exp(x))
        print("m: %.2f, %.2f" % (
            m - s*(stats.t.ppf(1-alpha/2, n-1))/np.sqrt(n-1),
            m + s*(stats.t.ppf(1-alpha/2, n-1))/np.sqrt(n-1)))
        print("sigma: %.2f, %.2f" % (
            s*np.sqrt(n)/np.sqrt(stats.chi2.ppf(1-alpha/2, n-1)),
            s*np.sqrt(n)/np.sqrt(stats.chi2.ppf(alpha/2, n-1))))
        print("m asymptotic :%.2f, %.2f" % (
            m - stats.norm.ppf(1-alpha / 2)/np.sqrt(n),
            m + stats.norm.ppf(1 - alpha / 2)/np.sqrt(n)))
        e = (sum(list(map(lambda el: (el-m)**4, x)))/n)/s**4 - 3
        print("sigma asymptotic: %.2f, %.2f" % (
                s/np.sqrt(1+stats.norm.ppf(1-alpha / 2)*np.sqrt((e+2)/n)),
                s/np.sqrt(1-stats.norm.ppf(1-alpha / 2)*np.sqrt((e+2)/n))))
    return

#task1_builder()
#task2_builder()
#task3_builder()
task4_builder()
