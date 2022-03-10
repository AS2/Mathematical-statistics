import numpy as np
import math as m

SAVE_PATH = "../docs/resources/"
ROUND_SIGNS = 8

def mean(data):
    return np.mean(data)

def median(data):
    return np.median(data)

def zR(data):
    size = len(data)
    return (data[0] + data[size - 1]) / 2

def zP(data, np):
    #return data[m.ceil(np)]
    if np.is_integer():
        return data[int(np)]
    else:
        return data[int(np) + 1]

def zQ(data):
    size = len(data)
    return (zP(data, size / 4) + zP(data, 3 * size / 4)) / 2

def zTR(data):
    size = len(data)
    r = int(size / 4)
    sum = 0
    for i in range(r + 1, size - r + 1):
        sum += data[i]
    return sum / (size - 2 * r)

def dispersion(data):
    return np.std(data) ** 2