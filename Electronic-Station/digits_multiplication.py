# coding: utf8
"""
Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.

Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).

example

Входные данные: Положительное целое число.

Выходные данные: Произведение цифр как целочисленное (int).

Примеры:

assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1
1
2
3
4
Зачем это нужно: Эта задача может научить вас как использовать простую конвертацию типов данных.

Предусловия: 0 < number < 106
"""


def checkio(number):
    result = 1
    if number > 0:
        for x in str(number):
            x = int(x)
            if x != 0:
                result *= x
            else:
                continue
    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
