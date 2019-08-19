"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

# В одномерном массиве найти сумму элементов, находящихся
# между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from memory_profiler import profile

@profile
def func():
    a = list(range(50000))
    # Попробовал добавить новую переменную new_a, но, т.к. она является ссылкой, дополнительной памяти не выделилось.
    new_a = a

    max_a = a[0]
    min_a = a[0]

    min_index = 0
    for i in range(len(new_a)):
        if min_a > new_a[i]:
            min_a = new_a[i]
            min_index = i
    print("Минимальный элемент: ", min_a)

    max_index = 0
    for i in range(len(new_a)):
        if max_a < new_a[i]:
            max_a = new_a[i]
            max_index = i
    print("Максимальный элемент: ", max_a)

    sum = 0

    if min_index > max_index:
        min_index, max_index = max_index, min_index

    for i in range(min_index + 1, max_index):
        sum += new_a[i]

    print(f"Сумма между минимальным и максимальным элементом массива {sum}")
    del a
    del new_a

if __name__== "__main__":
    func()

# Python 3.7 x64

"""
Line #    Mem usage    Increment   Line Contents
================================================
    17     13.3 MiB     13.3 MiB   @profile
    18                             def func():
    19     14.3 MiB      0.9 MiB       a = list(range(50000))
    20     14.3 MiB      0.0 MiB       new_a = a
    21                             
    22     14.3 MiB      0.0 MiB       max_a = a[0]
    23     14.3 MiB      0.0 MiB       min_a = a[0]
    24                             
    25     14.3 MiB      0.0 MiB       min_index = 0
    26     14.3 MiB      0.0 MiB       for i in range(len(new_a)):
    27     14.3 MiB      0.0 MiB           if min_a > new_a[i]:
    28                                         min_a = new_a[i]
    29                                         min_index = i
    30     14.3 MiB      0.0 MiB       print("Минимальный элемент: ", min_a)
    31                             
    32     14.3 MiB      0.0 MiB       max_index = 0
    33     14.3 MiB      0.0 MiB       for i in range(len(new_a)):
    34     14.3 MiB      0.0 MiB           if max_a < new_a[i]:
    35     14.3 MiB      0.0 MiB               max_a = new_a[i]
    36     14.3 MiB      0.0 MiB               max_index = i
    37     14.3 MiB      0.0 MiB       print("Максимальный элемент: ", max_a)
    38                             
    39     14.3 MiB      0.0 MiB       sum = 0
    40                             
    41     14.3 MiB      0.0 MiB       if min_index > max_index:
    42                                     min_index, max_index = max_index, min_index
    43                             
    44     14.3 MiB      0.0 MiB       for i in range(min_index + 1, max_index):
    45     14.3 MiB      0.0 MiB           sum += new_a[i]
    46                             
    47     14.3 MiB      0.0 MiB       print(f"Сумма между минимальным и максимальным элементом массива {sum}")
    48     14.3 MiB      0.0 MiB       del a
    49     13.5 MiB      0.0 MiB       del new_a
    
"""