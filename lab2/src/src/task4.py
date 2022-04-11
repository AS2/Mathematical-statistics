import numpy as np

def mean(data):
    return np.mean(data)

def dispersion_exp(sample):
    return mean(list(map(lambda x: x*x, sample))) \
           - (mean(sample))**2

def normal(size):
    return np.random.standard_normal(size=size)
