"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

i = 32
tab = ''
while i <= 127:
    if i % 10 != 2:
        tab += str(i) + ': ' + chr(i) + '   '
        i += 1
    else:
        tab += '\n' + str(i) + ': ' + chr(i) + '   '
        i += 1
print(tab)