"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import timeit

n = 900


# цикл
def summa_c(n):
    i = 1
    x = 1
    sum = 0
    while i <= n:
        if n == 0:
            print('no no no')
            break
        else:
            sum += x
            x /= -2
            i += 1
    return sum


# рекурсией
def sum_rec(n, i=0, sum=0):
    if i == n:
        return sum
    return sum_rec(n, i + 1, sum + (-1 / 2) ** i)


print(timeit.timeit("summa_c(n)", "from __main__ import summa_c, n", number=10000))
# 0.1656244 при n = 50
# 1.8187072 при n = 500
# 3.0577934 при n = 900

print(timeit.timeit("sum_rec(n)", "from __main__ import sum_rec, n", number=10000))
# 0.3003051 при n = 50
# 3.1599858999999997 при n = 500
# 5.7784534999999995 при n = 900
