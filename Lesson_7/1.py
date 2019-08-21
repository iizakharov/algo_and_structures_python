"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import timeit
import random

orig_list = [random.randint(-100, 100) for _ in range(20)]
# orig_list = [-85, -84, -65, -53, -43, -39, -31, -17, 3, 10, 13, 13, 38, 46, 74, 82, 87, 88, 94, 95]
print(orig_list)


def bubble_sort(arr):
    n = 0
    while n < len(orig_list):
        check = False
        for i in range(len(orig_list)-n):
            if i < len(orig_list) - n - 1:
                if orig_list[i] > orig_list[i+1]:
                    orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                    check = True
        if not check:
            break
        else:
            n += 1
    return arr


print(bubble_sort(orig_list))