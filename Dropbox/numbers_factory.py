'''
Дано число N . Необходимо найти наименьшее положительное целое число X , такое, что произведение его цифр будет равна N.
Если X не существует - верните 0.
Рассмотрим пример. N = 20. Мы можем разложить данное число, как 2*10, но 10 - это не цифра. Также можно разложить N,
как 4*5 или 2*2*5. Наименьшее число для 2*2*5 - это 225, для 4*5 -45. Результат 45.
Примечания: Не забудьте о простых числах и будьте аккуратны с вечными петлями.
Входные данные: Число N, как целое число (int).
Выходные данные: Число X, как целое число (int).

Примеры:

checkio(20) == 45
checkio(21) == 37
checkio(17) == 0
checkio(33) == 0

Зачем это нужно: В этой задаче вы попрактикуетесь работь с числами. А также можете сравнить, как решать задачи в лоб
или подумать более хитрое решение.

Предусловия:
9 < N < 10 5 .
'''


def checkio(number):
    result, divider = '', 9
    while divider > 1:
        if number % divider != 0:
            divider -= 1
        else:
             result = str(divider) + result
             number /= divider
    return int(result) if number == 1 else 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    # assert checkio(21) == 37, "2nd example"
    # assert checkio(17) == 0, "3rd example"
    # assert checkio(33) == 0, "4th example"
    # assert checkio(3125) == 55555, "5th example"
    # assert checkio(9973) == 0, "6th example"