"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from pympler import asizeof


class Car:
    def __init__(self, name):
        self.name = name
        self.year = 2019
        self.volume = 3500
        self.price = 2500000


class Car_slots:
    __slots__ = ['name', 'year', 'volume', 'price']

    def __init__(self, name):
        self.name = name
        self.year = 2019
        self.volume = 3500
        self.price = 2500000


car1 = Car('Genesis')
car2 = Car_slots('Genesis')

print(car1.__dict__)

print(asizeof.asizeof(car1))
print(asizeof.asizeof(car2))

# 312 - без слотов
# 120 - со слотами
# Вывод: слоты практически в три раза сэкономили память