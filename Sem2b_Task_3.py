# Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем. Программа должна возвращать сумму и произведение*
# дробей. Для проверки своего кода используйте модуль fractions.

import math
import fractions

fraction_1 = input("Введите числитель и знаменатель первого числа “a/b”: ")
fraction_2 = input("Введите числитель и знаменатель второго числа “a/b”: ")

# list_1 = a.split("/")
list_1 = [int(x) for x in fraction_1.split("/")]
num_1 = list_1[0]
den_1 = list_1[1]

list_2 = [int(x) for x in fraction_2.split("/")]
num_2 = list_2[0]
den_2 = list_2[1]

# умножение
multi_numerator = num_1 * num_2
multi_denominator = den_1 * den_2

# сложение
if den_1 == den_2:
    add_numerator = num_1 + num_2
    add_denominator = den_1
else:
    add_denominator = (den_1 * den_2) // (
        math.gcd(den_1, den_2))
    add_numerator = (num_1 * (
            add_denominator // den_1)) + (num_2 * (
            add_denominator // den_2))

# сокращение дробей
nod_1 = math.gcd(multi_numerator, multi_denominator)
nod_2 = math.gcd(add_numerator, add_denominator)

print(
    f"ПРОИЗВЕДЕНИЕ: {multi_numerator // nod_1}/{multi_denominator // nod_1}")
print(f"CУММА: {add_numerator // nod_2}/{add_denominator // nod_2}")
print("Проверка: ")
print((fractions.Fraction(num_1, den_1)) * (
    fractions.Fraction(num_2, den_2)))
print((fractions.Fraction(num_1, den_1)) + (
    fractions.Fraction(num_2, den_2)))
