# def no_mutable(a: int) -> int:
#     a += 1
#     print(f'In func {a = }') # Для демонстрации работы, но не для привычки
#     # принтить из функции
#     return a
# a = 42
# print(f'In main {a = }')
# z = no_mutable(a)
# print(f'{a = }\t{z = }')


# def from_one_to_n(n, data=None):
#     if data is None:   #особый прием для получения нового списка
#         data = []
#     for i in range(1, n + 1):
#         data.append(i)
#     return data
#
# new_list = from_one_to_n(5)
# print(f'{new_list = }')
# other_list = from_one_to_n(7)
# print(f'{other_list = }')

# def func(a=0.0, /, b=0.0, *, c=0.0):
#     """func(a=0.0: int | float, /, b=0.0: int | float, *, c=0.0:
# int | float) -> : int | float"""
#     if a > c:
#         return a
#     if a < c:
#         return c
#     return
# print(func(c=1, b=2, a=3))

# data = [25, -42, 146, 73, -100, 12]
# print(list(map(str, data)))
# print(max(data, key=lambda x: -x))
# print(data)
# print(*filter(lambda x: not x[0].startswith('__'),
# globals().items()))
#
# Напишите функцию, которая принимает строку текста. Вывести функцией каждое
# слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был
# один пробел между ним и номером строки

# def str_text(n:str)->str:
#     '''Работа со строкой.'''
#     b = ''
#     a = sorted(n.split())
#     max_len = 0
#     # max_len = len(max(a, key=len))
#     for el in a:
#         if len(el) > max_len:
#             max_len = len(el)
#     for n, el in enumerate(a, start=1):
#         b += f'{n} {el:>{max_len}}\n'
#     return b
#
# n = input()
# print(str_text(n))

# #Напишите функцию, которая принимает строку текста. Сформируйте список
# с уникальными кодами Unicode каждого символа введённой строки отсортированный
# по убыванию.
# def text_ord(n: str) -> list[int]:
#     d = set()
#     for el in n:
#         d.add(ord(el))
#     return sorted(list(d), reverse=True)
#
#
# n = input()
# print(text_ord(n))

# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

# def func(a: str) -> dict[str, int]:
#     new_dict = {}
#     start, stop = map(int, a.split())
#     for i in range(start, stop+1):
#         new_dict[chr(i)] = i
#     return new_dict
#
#
# a = "110 112"
# print(func(a))

# Функция получает на вход список чисел. Отсортируйте его элементы in place
# без использования встроенных в язык сортировок. Как вариант напишите
# сортировку пузырьком. Её описание есть в википедии.

# def sort_list(list_: list[int]):
#     for i in range(len(list_)):
#         print(f"i = {i}")
#         for j in range(i, len(list_)):
#             print(f"j = {j}")
#             if list_[i] > list_[j]:
#                 list_[i], list_[j] = list_[j], list_[i]
#
#
# list_ = [12, 34, 345, 54, 23]
# sort_list(list_)
# print(list_)


# Функция принимает на вход три списка одинаковой длины: имена str,
# ставка int, премия str с указанием процентов вида “10.25%”.
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве
# значения. Сумма рассчитывается как ставка умноженная на процент премии
def my_f(names: [str], salaries: [int], bonuses: [str]) -> dict[str, float]:
    result = {}
    for name, salary, bonus in zip(names, salaries, bonuses):
        result[name] = salary/100 * (float(bonus[:-1]))
    return result


n = ["Иван", "Николай", "Пётр", "Харитон"]
s = [125_000, 96_000, 109_000, 100_000]
a = ['10%', '25.5%', '13.3%', '42.73%']
print(my_f(n, s, a))







