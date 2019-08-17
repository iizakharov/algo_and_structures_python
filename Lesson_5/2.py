"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections

num = collections.defaultdict(list)
for i in range(2):
    n = input(f'Введите {i+1}-е 16-чное число: ')
    num[n] = list(n)
print(num)

summ = 0
multipl = 1
for i in num.values():
    summ += int(''.join(i), 16)
    multipl *= int(''.join(i), 16)
print('Сумма: ', list(str(hex(summ))[2:]))
print('Произведение: ', list(str(hex(multipl))[2:]))