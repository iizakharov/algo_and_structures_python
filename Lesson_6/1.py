"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

from memory_profiler import profile
import random


@profile
def cycle():
    k = 0
    array = []
    array_even = []

    for i in range(0, 1000000):
        array.append(random.randint(1, 20))

    for i in array:
        if i % 2 == 0:
            array_even.append(k)
        k += 1

    print(array)
    print(array_even)
    del array

cycle()

# Python 3.7 x64

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     14     14.1 MiB     14.1 MiB   @profile
#     15                             def cycle():
#     16     14.1 MiB      0.0 MiB       k = 0
#     17     14.1 MiB      0.0 MiB       array = []
#     18     14.1 MiB      0.0 MiB       array_even = []
#     19
#     20     17.8 MiB      0.0 MiB       for i in range(0, 1000000):
#     21     17.8 MiB      0.4 MiB           array.append(random.randint(1, 20))
#     22
#     23     32.0 MiB      0.1 MiB       for i in array:
#     24     32.0 MiB      0.0 MiB           if i % 2 == 0:
#     25     32.0 MiB      0.4 MiB               array_even.append(k)
#     26     32.0 MiB      0.1 MiB           k += 1
#     27
#     28     32.0 MiB      0.0 MiB       print(array)
#     29     32.0 MiB      0.0 MiB       print(array_even)
#     30     28.2 MiB      0.0 MiB       del array