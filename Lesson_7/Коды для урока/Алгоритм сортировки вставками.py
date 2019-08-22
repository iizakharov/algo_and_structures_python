import timeit
import random
from memory_profiler import memory_usage

def insertion_sort(orig_list):
    for i in range(len(orig_list)):
        v = orig_list[i]
        j = i

        while (orig_list[j-1] > v) and (j > 0):

            orig_list[j] = orig_list[j-1]
            j = j - 1

        orig_list[j] = v
    return orig_list


orig_list = [random.randint(-100, 100) for _ in range(500)]

# замеры
print(timeit.timeit("insertion_sort(orig_list)", \
    setup="from __main__ import insertion_sort, orig_list", number=10))




