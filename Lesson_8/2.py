"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

S = str(input("Введите строку: "))

print("Строка \'%s\' имеет длину: %d сиволов." % (S, len(S)))

my_set = set()
my_dict = {}
for i in range(len(S)):
    for j in range(len(S) - 1 if i == 0 else len(S), i, -1):
        my_set.add(hash(S[i:j]))
        my_dict[S[i:j]] = hash(S[i:j])

print(len(list(my_dict.keys())), list(my_dict.keys()))
print("Количество различных подстрок:", len(my_set))