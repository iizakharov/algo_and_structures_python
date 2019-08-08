"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
from random import random

N = 5
M = 4
matrix = []
step = 1

for i in range(M):
    arr = []
    sum = 0
    for j in range(N - 1):
        num = int(random() * 5)
        arr.append(num)
        sum += num
        # print(user_num, end=' ')
    arr.append(sum)
    print(f'Сумма 4-х элементов: {sum} добавлена в конец списка {step}')
    step +=1
    matrix.append(arr)
print('Получившаяся матрица:')
print(matrix)