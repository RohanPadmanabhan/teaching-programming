from matplotlib import pyplot as plt
from random import randint
from time import clock
from random import randrange
import numpy as np
from utils import time_f, reject_outliers

def time_sorts(lower, upper, steps, sorts, sort_labels):
    # Create a list with lists of times for each sorting algorithm
    times = [[] for _ in range(len(sorts) + 1)]
    
    # Loop to a list of size n
    for i in range(lower, upper, steps):
        # Apply each sort 
        for sort_index, sort in enumerate(sorts):
            unavg_time = []
            # Average the time over 100 sorts of the list
            for j in range(100):
                rand_list_temp = [randrange(0, 2000) for _ in range(i)]
                runtime = time_f(lambda: sort(rand_list_temp))
                unavg_time.append(runtime)
            
            # Calculate and save the average runtime (without outliers)
            unavg_time = reject_outliers(unavg_time)
            avg_runtime = sum(unavg_time) / len(unavg_time)
            times[sort_index].append(avg_runtime)
    return times

def benchmark_sorts(sorts, lower, upper, steps):
    # Get list of sort names
    sort_labels = [sort.__name__ for sort in sorts]
    # Calculate sort times
    times = time_sorts(lower, upper, steps, sorts, sort_labels)
    
    # Plot each sorting algorithm with its name
    for index, sort_label in enumerate(sort_labels):
        plt.plot(range(lower, upper, steps), times[index], label=sort_label)
        
    # Add axis labels and legend
    plt.xlabel('n')
    plt.ylabel('time (/s)')
    plt.legend(sort_labels)
    
    plt.show()

def test_sort(sort_func):
    
    n = 100
    x = [randint(0, n) for _ in range(n)]

    sort_name = sort_func.__name__
    if is_sorted(sort_func(x)):
        print(sort_name + " works!")
    else:
        print(sort_name + " has failed.")

def is_sorted(l):
    return all([l[i] <= l[i+1] for i in range(len(l)-1)])

