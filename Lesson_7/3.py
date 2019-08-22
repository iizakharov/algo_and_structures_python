"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

from random import randint

m = 5
arr = [randint(0, 100) for _ in range(2*m + 1)]
print('Исходный массив: ' + str(arr))
new_arr = arr


def cocktail_sort(orig_list):
    left = 0
    right = len(orig_list) - 1
    while left <= right:
        for i in range(left, right):
            if orig_list[i] > orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        right -= 1
        for i in range(right, left, -1):
            if orig_list[i-1] > orig_list[i]:
                orig_list[i], orig_list[i-1] = orig_list[i-1], orig_list[i]
        left += 1
    return orig_list


print('Отсортированный массив "Шейкером": ' + str(cocktail_sort(new_arr)))


def median(orig_list):
    for i in range(len(orig_list)):
        l, m, r = 0, 0, 0
        for j in range(len(orig_list)):
            if orig_list[j] > orig_list[i]:
                r += 1
            elif orig_list[j] < orig_list[i]:
                l += 1
            else:
                m += 1
        if abs(l - r) <= (m - 1):
            return orig_list[i]


print('Медианой данного массива будет число: ' + str(median(new_arr)))
