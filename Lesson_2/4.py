"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

n = int(input('Введите число: '))

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
print(sum)


# рекурсией
def sum(x, n):
    if n > 1:
        return x + sum(x / (-2), n - 1)
    elif n == 1:
        return x


n = int(input("Сколько раз? "))
print(sum(1, n))