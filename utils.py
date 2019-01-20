from matplotlib import pyplot as plt
from random import randint
from time import clock
from random import randrange
import numpy as np

# a timer - runs the provided function and reports the
# run time in ms
def time_f(f):
    before = clock()
    f()
    after = clock()
    return after - before

def reject_outliers(data):
    m = 1.5
    u = np.mean(data)
    s = np.std(data)
    filtered = [e for e in data if (u - m * s < e < u + m * s)]
    return filtered