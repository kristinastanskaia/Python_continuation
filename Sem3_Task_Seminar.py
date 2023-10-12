# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# print(my_list[2:6:2])
# print(my_list.pop())
# print(my_list.extend([314, 42]))
# print(my_list.sort(reverse=False))
# print(my_list)

# text = 'Привет, мир!'
# print(text.find(' '))
# print(text.title())
# print(text.split())
# print(f'{text = :>25}')

# my_dict = {'one': 1,
#  'two': 2,
#  'three': 3,
#  'four': 4,
#  'ten': 10,
#  }
# print(my_dict.setdefault('ten', 555))
# print(my_dict.values())
# print(my_dict.pop('one'))
# my_dict['one'] = my_dict['four']
# print(my_dict)

# my_set = frozenset({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
# print(len(my_set))
# print(my_set - {1, 2, 3})
# print(my_set.union({2, 4, 6, 8}))
# print(my_set & {2, 4, 6, 8})
# print(my_set.discard(10))

# text_en = 'Hello world!'
# res = text_en.encode('utf-8')
# print(res, type(res))
# text_ru = 'Привет, мир!'
# res = text_ru.encode('utf-8')
# print(res, type(res))

# n = input()
# a = sorted(n.split())
# max_len = 0
# for el in a:
#     if len(el) > max_len:
#         max_len = len(el)
#
# for n, el in enumerate(a, start=1):
#     print(f'{n} {el:>{max_len}}')

# ищет в списке самое длинное слово и возвращает его длину
# max_len = len(max(a, key=len))

hike = {
    'Aaz': ("спички", "спальник", "дрова", "топор"),
    'Skeeve': ("спальник", "спички", "вода", "еда"),
    'Tananda': ("вода", "спички", "косметичка"),
}

# result = set()
# for i in hike.values():
#     if result == set():
#         result = set(i)
#     else:
#         result = result & set(i)
# print(result)

# hike = {
# 'Aaz': ("спальник", "дрова", "топор", "еда"),
# 'Skeeve': ("спальник", "спички", "вода", "еда"),
# 'Tananda': ("вода", "косметичка", "еда"),
# 'Tanan': ("вода", "спички", "косметичка"),
# }
#
# result = set()
# for i in hike.values():
#     if result == set():
#         result = set(i)
#     else:
#         result = result & set(i)
# # print(result)
#
# only_one = set()
# for i in hike.values():
#     only_one = set(i)
#     for j in hike.values():
#         if i == j:
#             continue
#         else:
#             only_one -= set(j)
# # print(only_one)
#
# for name, i in hike.items():
#     not_one = None
#     for j in hike.values():
#         if i == j:
#             continue
#         elif not not_one and not_one != set():
#             not_one = set(j)
#         else:
#             not_one &= set(j)
#
#     print(name, not_one - set(i))


# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2] -> [1, 2]

# my_list = [2, 4, 2, 3, 3, 0, 16, 3, 0]
# new_list = []
# for i in set(my_list):
#     if my_list.count(i) > 1:
#         new_list.append(i)
# print(new_list)

text = "Добрый день! Я впечатлена вашей компанией и интересными задачами, " \
       "которые вы решаете! Мой опыт в управлении проектами, способность " \
       "эффективно использовать ресурсы и достигать целей стали неотъемлемой " \
       "частью моей профессиональной истории. Мне нравится изучать новые " \
       "области и преодолевать вызовы, поэтому недавно я успешно завершила" \
       " курс «Тестирование ПО» и приобрела ключевые знания и практический" \
       " опыт в области тестирования программного обеспечения. С нетерпением " \
       "ожидаю возможности познакомиться и стать частью вашей команды!"
new_text = text.replace(".", "")
new_text = new_text.lower()
new_text = new_text.split()
new_dict = dict()
print(new_text)
for i in set(new_text):
    count_i = new_text.count(i)
    new_dict[i] = count_i

sort_dict = dict(
    sorted(new_dict.items(), key=lambda item: item[1], reverse=True))
print(sort_dict)
count = 0
for key, value in sort_dict.items():
    if count < 10:
        print(f'Слово "{key}", {value} раз')
        count += 1
    else:
        break

