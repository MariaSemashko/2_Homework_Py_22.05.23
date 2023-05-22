# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

try:
    n = int(input("Введите положительное число: "))
    flag = True
    while flag:
        if n > 0:
            flag = False
        else:
            n = int(input("Некорректный ввод. Введите положительное число: "))

    k = 0
    while 2**k < n:
        print(2**k)
        k +=1
except ValueError:
    print("Вы ввели не число")
