# so our plots get drawn in the notebook
from matplotlib import pyplot as plt
from random import randint
from time import clock
from random import randrange
import numpy as np
from utils import time_f, reject_outliers

def time_searches(lower, upper, steps, searches):
    # Create a list with lists of times for each searching algorithm
    times = [[] for _ in range(len(searches) + 1)]
    
    # Loop to a list of size n
    for i in range(lower, upper, steps):
        # Apply each search 
        for search_index, search in enumerate(searches):
            unavg_time = []
            # Average the time over 500 searches of the list
            for j in range(500):
                ordered_list_temp = [num for num in range(i)]
                runtime = time_f(lambda: search(ordered_list_temp, randint(0, i-1)))
                unavg_time.append(runtime)
            
            # Calculate and save the average runtime (without outliers)
            unavg_time = reject_outliers(unavg_time)
            avg_runtime = sum(unavg_time) / len(unavg_time)
            times[search_index].append(avg_runtime)
    return times

def benchmark_searches(searches, lower, upper, steps):
    # Get list of search names
    search_labels = [search.__name__ for search in searches]
    # Calculate search times
    times = time_searches(lower, upper, steps, searches)
    
    # Plot each searching algorithm with its name
    for index, search_label in enumerate(search_labels):
        plt.plot(range(lower, upper, steps), times[index], label=search_label)
        
    # Add axis labels and legend
    plt.xlabel('n')
    plt.ylabel('time (/s)')
    plt.legend(search_labels)
    
    plt.show()

    
def test_search(search_func):
    # Build an ordered array of values
    n = 100
    x = [i for i in range(n)]
    act_index = randint(0, n-1)

    search_name = search_func.__name__
    positive_success = search_func(x, x[act_index]) == act_index
    negative_success = search_func(x, n+1) == None
    
    
    if positive_success and negative_success:
        print(search_name + " works!")
    else:
        print(search_name + " has failed.")