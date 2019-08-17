"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
from collections import defaultdict

firm_count = int(input('Введите количество предприятий: '))
my_dict = defaultdict(list)
profit_sum = defaultdict(list)
for index in range(1, firm_count + 1):
    name = input(f'Введите наименование предприятия {index}: ')
    for quarter in range(1, 5):
        my_dict[name].append(float(input(f'Введите прибыль за {quarter} квартал: ')))
    profit_sum[name] = (sum(my_dict[name]))
profit_average = sum(profit_sum.values()) / firm_count

print(my_dict)
print(profit_sum)
print(f'Средня прибыль по всем предприятиям: {profit_average}')

above_average = []
below_average = []
for enterpise in my_dict:
    if profit_sum[enterpise] > profit_average:
        above_average.append(enterpise)
    elif profit_sum[enterpise] < profit_average:
        below_average.append(enterpise)
print(f'Предприятия, чья прибыль выше среднего: {", ".join(above_average)}')
print(f'Предприятия, чья прибыль ниже среднего: {", ".join(below_average)}')