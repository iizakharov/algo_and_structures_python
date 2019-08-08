#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random

arr = [random.choice([i for i in range(100)]) for j in range(20)]
# arr = [2, 21, 97, 26, 97, 2, 94, 14, 51, 28]
min = 100
max = 0

for i in arr:
    if max < i:
        max = i
    if min > i:
        min = i
print(arr)
print(f'Минимальное число массива: {min}')
print(f'Максимальное число массива: {max}')

for j in range(len(arr)):
    if arr[j] == max:
        a = j
        break
for j in range(len(arr)):
    if arr[j] == min:
        b = j
        break

arr[a], arr[b] = arr[b], arr[a]

print(arr)
