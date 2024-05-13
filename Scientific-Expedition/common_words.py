# coding: utf8

'''
Продолжим изучение слов. Даны две строки со словами, разделенными запятыми.
Попробуйте найти что общего между этими строками. Слова внутри каждой строки не повторяются.

Ваша функция должна находить все слова, которые появляются в обеих строках.
Результат должен быть представлен, как строка со словами разделенными запятыми и отсортированными в алфавитном порядке.

Вх. данные: Два аргумента как строки (str).

Вых. данные: Общие слова как строка (str).

Примеры:

assert checkio("hello,world", "hello,earth") == "hello"
assert checkio("one,two,three", "four,five,six") == ""
assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

Как это используется: В этой задаче вы попрактикуетесь в работе с наборами и строками.
И эти навыки будут полезными для лингвистического анализа.

Предусловия:
Каждая строка содержит не более 10 слов.
Все слова разделены запятыми.
Все слова состоят только из латинских букв в нижнем регистре.
'''

def checkio(first, second):

    first = set(first.split(","))
    second = set(second.split(","))

    return ",".join(sorted(first & second))   # Можно писать и так: first.intersection(second)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"