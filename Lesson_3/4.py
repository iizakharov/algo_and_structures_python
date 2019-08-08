# 4.	Определить, какое число в массиве встречается чаще всего.

from random import random

N = 10
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 5)
print(arr)

num = arr[0]
max_rep = 1
for i in range(N - 1):
    rep = 1
    for k in range(i + 1, N):
        if arr[i] == arr[k]:
            rep += 1
    if rep > max_rep:
        max_rep = rep
        num = arr[i]

if max_rep > 1:
    print(max_rep, 'раз(a) встречается число', num)
else:
    print('Все числа уникальны')