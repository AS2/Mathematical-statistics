from normal_dist import plot_normal
from uniform_dist import plot_uniform
from cauсhy_dist import plot_cauchy
from poisson_dist import plot_poisson

SIZES = [10, 100, 1000]
M = 10.0
begin = -1.5
length = begin * 2


plot_normal(SIZES, "normal nums", "denstiny", "skyblue")
plot_uniform(begin, length, SIZES, "uniform nums", "denstiny", "royalblue")
plot_cauchy(SIZES, "cauchy nums", "denstiny", "cyan")
plot_poisson(M, SIZES, "poisson nums", "denstiny", "pink")