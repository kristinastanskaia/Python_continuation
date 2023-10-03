# задачи на семинаре №2

# Напишите программу, которая вычисляет площадь круга и длину окружности по
# введённому диаметру. Диаметр не превышает 1000 у.е. Точность вычислений должна
# составлять не менее 42 знаков после запятой.

import decimal
import math

# decimal.getcontext().prec = 42
# d = decimal.Decimal(input("введите диаметр: "))
# pi = decimal.Decimal(math.pi)
#
# s = pi * pow(d, 2) / 4
# l = pi * d
#
# print(s, l)

# Напишите программу, которая решает квадратные уравнения даже если дискриминант
# отрицательный. Используйте комплексные числа для извлечения квадратного корня.

# a = 5
# b = 8
# c = -20
# d = b ** 2 - 4 * a * c
# x1 = (- b + d ** 0.5) / 2 * a
# x2 = (- b - d ** 0.5) / 2 * a
#
# print(x1, x2)
# print(type(x1), type(x2))

# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной. Любое действие выводит сумму денег

s = 10000
count = 0
RICHLIMIT = 5_000_000
RICHTAX = 0.9
THREEOPERATIONS = 3
BONUSTHREE = 1.03
FREENDERING = 50
COMMISSIONOUTDROW = 0.015
MINLIMIT = 30
MAXLIMIT = 600

while True:
    action = input('Введите операцию 1(пополнение),2(снятие),3(выход): ')
    if s >= RICHLIMIT:
        s *= RICHTAX
    if count % THREEOPERATIONS == 0 and count != 0:
        s *= BONUSTHREE
        count = 0
    if action == '1':
        withdrow = int(input('введиет сумму: '))
        if withdrow % FREENDERING == 0:
            count += 1
            s += withdrow
    elif action == '2':
        withdrow = int(input('введиет сумму: '))
        if withdrow % FREENDERING == 0:
            comission = withdrow * COMMISSIONOUTDROW
            if comission < MINLIMIT:
                comission = MINLIMIT
            elif comission > MAXLIMIT:
                comission = MAXLIMIT
            if (comission + withdrow) < s:
                s -= (withdrow + comission)
        count += 1
    else:
        break
    print(s)
