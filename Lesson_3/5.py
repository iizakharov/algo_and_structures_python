#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

import random

N = 10
arr = [0] * N
for i in range(N):
    arr[i] = random.randint(-20, 20)
print(arr)

# arr = [-7, -4, -8, 8, -2, 8, 6, -10, 9, -1]
answer = min(arr)
for i in range(len(arr)):
    if (arr[i] < 0) and (arr[i] > answer):
        answer = arr[i]

print('Максимально отрицательное число: ',answer)
