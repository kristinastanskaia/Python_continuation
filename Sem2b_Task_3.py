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
multiplication_numerator = num_1 * num_2
multiplication_denominator = den_1 * den_2

# сложение
if den_1 == den_2:
    addition_numerator = num_1 + num_2
    addition_denominator = den_1
else:
    addition_denominator = (den_1 * den_2) // (
        math.gcd(den_1, den_2))
    addition_numerator = (num_1 * (
            addition_denominator // den_1)) + (num_2 * (
            addition_denominator // den_2))

# сокращение дробей
nod_1 = math.gcd(multiplication_numerator, multiplication_denominator)
nod_2 = math.gcd(addition_numerator, addition_denominator)

print(
    f"ПРОИЗВЕДЕНИЕ: {multiplication_numerator // nod_1}/{multiplication_denominator // nod_1}")
print(f"CУММА: {addition_numerator // nod_2}/{addition_denominator // nod_2}")
print("Проверка: ")
print((fractions.Fraction(num_1, den_1)) * (
    fractions.Fraction(num_2, den_2)))
print((fractions.Fraction(num_1, den_1)) + (
    fractions.Fraction(num_2, den_2)))
