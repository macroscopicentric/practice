import random
import time

source_list = [random.randint(0, 100000) for i in range(2000)]
# source_list = [53, 85, 49, 15, 50, 17, 75, 6, 39, 99, 38, 89, 27, 82, 95, 62, 51, 42, 3, 27]

def n_squared():
    start = time.time()
    smallest_number = 100
    for i in source_list:
        for j in source_list:
            tmp = min(i,j)
            if tmp < smallest_number:
                smallest_number = tmp
    end = time.time()
    return "Time spent: %s seconds." % (round(end - start, 10)), smallest_number

def linear_n():
    start = time.time()
    smallest_number = source_list[0]
    for num in source_list:
        if num < smallest_number:
            smallest_number = num
    end = time.time()
    return "Time spent: %s seconds." % (round(end - start, 10)), smallest_number

print n_squared()
print linear_n()