# Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем. Программа должна возвращать сумму и произведение*
# дробей. Для проверки своего кода используйте модуль fractions.

first_num = input("Введите числитель и знаменатель первого числа “a/b”: ")
second_num = input("Введите числитель и знаменатель первого числа “a/b”: ")

# list_1 = a.split("/")
first_list = [int(x) for x in first_num.split("/")]
second_list = [int(x) for x in second_num.split("/")]

# умножение
multiplication_numerator = first_list[0] * second_list[0]
multiplication_denominator = first_list[1] * second_list[1]

# сложеине
if first_list[1] == second_list[1]:
    addition = first_list[0] + second_list[0]
else:
    addition == 1

print(f"{multiplication_numerator}/{multiplication_denominator}")
print(f"{addition}/{first_list[1]}")
