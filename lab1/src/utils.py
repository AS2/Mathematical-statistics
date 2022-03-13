import numpy as np
import math as m
import seaborn as sns
import matplotlib.pyplot as plt

SAVE_PATH = "../docs/resources/"
ROUND_SIGNS = 8

# task 2 utils
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

# task 3 utils
def moustaches(data):
    q_1, q_3 = np.quantile(data, [0.25, 0.75])
    return q_1 - 3 / 2 * (q_3 - q_1), q_3 + 3 / 2 * (q_3 - q_1)

def number_of_emissions(data):
    x1, x2 = moustaches(data)
    filtered = [x for x in data if x > x2 or x < x1]
    return len(filtered)

def draw_boxplot_Tukey(tips, name : str):
    plt.clf()
    sns.set_theme(style="whitegrid")    
    sns.boxplot(data=tips, palette='rainbow', orient='h')
    sns.despine(offset=10)
    plt.xlabel("x")
    plt.ylabel("n")
    plt.title(name)
    #plt.show()
    plt.savefig(SAVE_PATH + str(name)+".jpg")
    return

def print_emissions(sizes : list, result : list):
    print("Emmisions[from" + str(sizes[0]) + " power selection]: " + str(result[0]))
    print("Emmisions[from" + str(sizes[1]) + " power selection]: " + str(result[1]))