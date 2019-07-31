#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

let_1 = ord(input("Введите первый символ "))
let_2 = ord(input("Введите второй символ "))

if let_1 > let_2:
    distance = (let_1 - let_2) - 1

elif let_1 < let_2:
    distance = (let_2 - let_1) - 1
elif let_1 == let_2:
    print("Буквы совпадают")
print('Между данными буквами еще {} букв(a)'.format(distance))

place1 = let_1 - ord('a') + 1
place2 = let_2 - ord('a') + 1
print(place1, place2)
