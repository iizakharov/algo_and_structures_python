"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random
N = 10
arr = [random.choice([i for i in range(10)]) for j in range(N)]
# arr = [18, 99, 19, 78, 51, 71, 2, 59, 13, 90]
min_num = min(arr)
max_num = max(arr)

for j in range(len(arr)):
    if arr[j] == min_num:
        min = j
        break
for j in range(len(arr)):
    if arr[j] == max_num:
        max = j
        break

print(arr)
print(f'Минимальное число массива: {min_num} на позиции № {min + 1} из {N}')
print(f'Максимальное число массива: {max_num} на позиции № {max + 1} из {N}')

sum = 0
if min < max:
    while min != max - 1:
        min += 1
        sum += arr[min]
elif min > max:
    while max != min - 1:
        max += 1
        sum += arr[max]
if sum == 0:
    print('Между числами нет элементов, они идут друг за другом!')
else:
    print(f'Сумма чисел между ними {sum}')

