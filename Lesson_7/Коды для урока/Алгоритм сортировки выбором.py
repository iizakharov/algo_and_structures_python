import timeit
import random

def selection_sort(orig_list):
    for i in range(len(orig_list)):
        idx_min = i
        for j in range(i+1, len(orig_list)):
            if orig_list[j] < orig_list[idx_min]:
                idx_min = j

        tmp = orig_list[idx_min]
        orig_list[idx_min] = orig_list[i]
        orig_list[i] = tmp

    return orig_list


orig_list = [random.randint(-100, 100) for _ in range(500)]

# замеры
print(timeit.timeit("selection_sort(orig_list)", \
    setup="from __main__ import selection_sort, orig_list", number=10))




