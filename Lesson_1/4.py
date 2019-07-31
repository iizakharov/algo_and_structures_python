"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
import random

turn = int(input("Случайное целое число - введите 1 \n"
                 "Случайное вещественное число - введите 2 \n"
                 "Случайный символ - введите 3 \n"))
if turn == 1:
    min_number = int(input('Введите минимальное число:'))
    max_number = int(input('Введите максимальное число:'))

    random_number = random.randint(min_number, max_number + 1)
    print('Случайное целое число: {}'.format(random_number))

elif turn == 2:
    min_number = int(input('Введите минимальное число:'))
    max_number = int(input('Введите максимальное число:'))

    random_number_2 = random.uniform(min_number, max_number + 1)
    print('Случайное вещественное число: {}'.format(random_number_2))

elif turn == 3:
    min_letter = str(input('Введите первую букву:'))
    max_letter = str(input('Введите последнюю букву:'))

    random_letter = random.randint(ord(min_letter), ord(max_letter))
    print('Случайная буква: {}'.format(chr(random_letter)))

else:
    print("Нужно было ввести либо 1, либо 2, било 3")

