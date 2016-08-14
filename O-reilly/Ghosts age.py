# coding: utf8


def checkio(opacity):

    # Создаём список из чисел Фибоначчи
    fibonacci = [0, 1]
    while len(fibonacci) < 21:
        fibonacci.append(fibonacci[-1]+fibonacci[-2])

    maxOpacity = 10000
    age = 0

    while maxOpacity != opacity:
        age += 1
        if age in fibonacci:
            maxOpacity -= age
        else:
            maxOpacity += 1

    return age

# ---------------------------------------------------------------------------------------------
#                                       Этот вариант со словарями
#
# def checkio(opacity):
#
#     # Создаём список из чисел Фибоначчи
#     fibonacci = [0, 1]
#     while len(fibonacci) < 21:
#         fibonacci.append(fibonacci[-1]+fibonacci[-2])
#
#     # Пришлось создать 2 словаря, дублирующих друг друга, но зеркально, что бы получать и значения и ключи
#     ghost_dict = {10000: 0,}
#     ghost_dict_dupl = {0:10000}
#     age = 0
#
#
#     for x in range(0, 5000):
#
#         age += 1
#
#         if age in fibonacci:
#             znac_prozrachnosti = ghost_dict_dupl[age - 1]       # Получаем прозрачность от предыдущего периода (из дублирующего словаря)
#             ghost_dict[znac_prozrachnosti - age] = age          # Вычитаем возраст и записываем в словарь
#             ghost_dict_dupl[age] = znac_prozrachnosti - age     # Тут просто дублируем предыдущую строчку но для дублирующего словаря
#             x += 1
#
#         else:
#             znac_prozrachnosti = ghost_dict_dupl[age - 1]       # Тоже самое что в IF'e, но к прозрачности прибавляем 1
#             ghost_dict[znac_prozrachnosti + 1] = age
#             ghost_dict_dupl[age] = znac_prozrachnosti + 1
#             x += 1
#
#     return ghost_dict[opacity]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"