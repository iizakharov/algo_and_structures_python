"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import timeit
import random

arr = [random.random() * 50 for _ in range(20)]
print(arr)


def merge_sort(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        return orig_list


def merge_sort_2(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        sort_arr = []
        i, j, = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sort_arr.append(left[i])
                i += 1
            else:
                sort_arr.append(right[j])
                j += 1
        sort_arr += left[i:]
        sort_arr += right[j:]
        return sort_arr

# замеры

print(merge_sort(arr))
print(merge_sort_2(arr))
print(timeit.timeit("merge_sort(arr)", \
    setup="from __main__ import merge_sort, arr", number=10))