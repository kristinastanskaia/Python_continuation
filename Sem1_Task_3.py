# 3. Напишите код, который запрашивает число и сообщает является ли оно простым
# или составным. Используйте правило для проверки: “Число является простым,
# если делится нацело только на единицу и на себя”. Сделайте ограничение на
# ввод отрицательных чисел и чисел больше 100 тысяч.

# num = int(input("Введите число: "))
# number_description = "простое"
# if 1 < num <= 100000:
#     for i in range(2, num):
#         if num % i > 0:
#             continue
#         else:
#             number_description = "составное"
#     print(number_description)
# else:
#     print("Число не подходит!")

num = int(input("Введите число: "))
number_description = "простое"
if 1 < num <= 100000:
    for i in range(2, num):
        if num % i == 0:
            number_description = "составное"
            break
    print(number_description)
else:
    print("Число не подходит!")
