import timeit
import random

def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] > orig_list[i+1]:
                orig_list[i],orig_list[i+1] = orig_list[i+1],orig_list[i]
        n += 1
    return orig_list


# замеры
orig_list = [random.randint(-100, 100) for _ in range(500)]

print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=10))


