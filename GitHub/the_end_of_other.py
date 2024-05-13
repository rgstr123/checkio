# coding: utf8
'''
Для практики в лингвистике Роботы хотят изучить суффиксы.
В этой задаче дан набор слов в нижнем регистре. Проверьте есть ли в этом наборе пара слов, такая что одно слово
заканчивается другим (суффикс или совпадение). Для примера: {"hi", "hello", "lo"} -- "lo" это окончание "hello",
так что результат True.
Замечания: Для этой задачи вы можете прочитать о типе данных set и строковых функциях .
Вх. данные: Слова как набор (set) строк (str).
Вых. данные: True или False, как булево выражение.

Примеры:

checkio({"hello", "lo", "he"}) == True
checkio({"hello", "la", "hellow", "cow"}) == False
checkio({"walk", "duckwalk"}) == True
checkio({"one"}) == False
checkio({"helicopter", "li", "he"}) == False

Как это используется: В этой задаче вы познакомитесь с тем, как итерировать тип данных set и некоторыми полезными
функциями.

Предусловия: 2 ≤ len(words) < 30
all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)

Каждый игрок может создавать свои задачи на Checkio, начиная с 9ого уровня. У вас есть возможность создать головоломки
для ваших друзей.
'''


def checkio(words_set):
    lst = list(words_set)
    flag = False

    for first in lst:
        for second in lst:
            if first == second:
                continue
            if second.endswith(first):
                flag = True
    return flag


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
