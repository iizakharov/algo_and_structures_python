"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import random

N = 10
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 10)

if arr[0] < arr[1]:
    min_1 = arr[0]
    min_2 = arr[1]
else:
    min_1 = arr[1]
    min_2 = arr[0]
for i in range(2, len(arr)):
    if arr[i] <= min_1:
        min_2 = min_1
        min_1 = arr[i]
    elif arr[i] < min_2:
        min_2 = arr[i]
print(arr)
if min_1 == min_2:
    print(f'оба минимальных числа имеют значение: {min_1}')
else:
    print(f'Первое минимальное число = {min_1}, второе минимальное число = {min_2}')