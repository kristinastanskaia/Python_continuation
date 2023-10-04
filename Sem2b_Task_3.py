# Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем. Программа должна возвращать сумму и произведение*
# дробей. Для проверки своего кода используйте модуль fractions.

import math

num_1 = input("Введите числитель и знаменатель первого числа “a/b”: ")
num_2 = input("Введите числитель и знаменатель первого числа “a/b”: ")

# list_1 = a.split("/")
list_1 = [int(x) for x in num_1.split("/")]
list_2 = [int(x) for x in num_2.split("/")]

# умножение
multiplication_numerator = list_1[0] * list_2[0]
multiplication_denominator = list_1[1] * list_2[1]

# сложение
if list_1[1] == list_2[1]:
    addition_numerator = list_1[0] + list_2[0]
    addition_denominator = list_1[1]
else:
    addition_denominator = (list_1[1] * list_2[1]) // (
        math.gcd(list_1[1], list_2[1]))
    addition_numerator = (list_1[0] * (
            addition_denominator // list_1[1])) + (list_2[0] * (
            addition_denominator // list_2[1]))

print(
    f"ПРОИЗВЕДЕНИЕ: {multiplication_numerator}/{multiplication_denominator}")
print(f"CУММА: {addition_numerator}/{addition_denominator}")
