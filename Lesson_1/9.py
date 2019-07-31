# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

if a == b or a == c or b == c:
    print("Числа равны")
else:
    if a > b:
        if a < c:
            print("Число {} является средним".format(a))
        elif c > b:
            print("Число {} является средним".format(c))
        else:
            print("Число {} является средним".format(b))
    else:
        if b < c:
            print("Число {} является средним".format(b))
        elif a < c:
            print("Число {} является средним".format(c))
        else:
            print("Число {} является средним".format(a))
