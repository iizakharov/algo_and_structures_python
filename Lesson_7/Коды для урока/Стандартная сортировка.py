import timeit
import random

def reverse_sort(orig_list):
    ordered_list = sorted(orig_list)
    return ordered_list

orig_list = [random.randint(-100, 100) for _ in range(500)]
print(timeit.timeit("reverse_sort(orig_list)", setup = "from __main__ import reverse_sort, orig_list", number=10))







