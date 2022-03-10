from normal_dist import plot_normal, print_table_normal
from uniform_dist import plot_uniform, print_table_uniform
from cauсhy_dist import plot_cauchy, print_table_cauchy
from poisson_dist import plot_poisson, print_table_poisson

# LAB-1
# Task #1 - build distributions
SIZES = [10, 100, 1000]
M = 10.0
begin = -1.7320508
length = begin * 2
plot_normal(SIZES, "normal nums", "denstiny", "skyblue")
plot_uniform(begin, length, SIZES, "uniform nums", "denstiny", "royalblue")
plot_cauchy(SIZES, "cauchy nums", "denstiny", "cyan")
plot_poisson(M, SIZES, "poisson nums", "denstiny", "pink")

# Task #2 - build characteristics values of different distributions
repeats = 1000
print_table_normal(SIZES, repeats)
print("\n")
print_table_uniform(SIZES, repeats)
print("\n")
print_table_cauchy(SIZES, repeats)
print("\n")
print_table_poisson(M, SIZES, repeats)