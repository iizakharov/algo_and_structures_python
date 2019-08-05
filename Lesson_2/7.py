"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def rec(n):
    if n != 0:
        return n + rec(n-1)
    elif n == 0:
        return n


n = int(input("Введите натуральное число: "))

first = n * (n + 1) // 2
second = rec(n)
if second == first:
    print(f"{second} = {first} \nРавенство 1+2+...+n = n(n+1)/2 действительно выполняется")