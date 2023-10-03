# 2. Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для
# проверки своего результата.


# Получаем целое число от пользователя
num = int(input("Введите целое число: "))
examination = hex(num)
result = ""
# Создаем строку с шестнадцатеричными символами
hex_chars = "0123456789abcdef"

# Пока число больше 0, вычисляем
while num > 0:
    digit = num % 16  # Получаем остаток от деления на 16
    digit = hex_chars[digit]  # Получаем соответствующую цифру
    result = digit + result
    num //= 16  # Делаем целочисленное деление на 16 для следующей итерации
if result == "":  # Если число было равно 0, то шестнадцатеричное представление - "0"
    result = "0"

print("0x" + result)
print(examination)



# другие варианты
# a = int(input("Введите целое число: "))
# el = "0x"
# b = hex(a)
# result = ""
# while a > 0:
#     if a % 16 == 10:
#         result = "a" + result
#     elif a % 16 == 11:
#         result = "b" + result
#     elif a % 16 == 12:
#         result = "c" + result
#     elif a % 16 == 13:
#         result = "d" + result
#     elif a % 16 == 14:
#         result = "e" + result
#     elif a % 16 == 15:
#         result = "f" + result
#     else:
#         result = str(a % 16) + result
#     a = a // 16
#
# print(f'{el}{result}')
# print(b)

# print(el + result)
# преобразование в список (добавили нулевой элемен в список и обьединили
# список в строку)
# num = list(result)
# (num).insert(0, el)
# print(''.join(num))


# a = int(input("Введите целое число: "))
# el = "0x"
# b = hex(a)
# result = ""
# while a > 0:
#     g = a % 16
#     if g == 10:
#         ost = "a"
#     elif g == 11:
#         ost = "b"
#     elif a % 16 == 12:
#         ost = "c"
#     elif a % 16 == 13:
#         ost = "d"
#     elif a % 16 == 14:
#         ost = "e"
#     elif a % 16 == 15:
#         ost = "f"
#     else:
#         ost = g
#     result = str(ost) + result
#     a = a // 16
#
# print(f'{el}{result}')
# print(b)




