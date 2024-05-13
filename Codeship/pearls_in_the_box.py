# coding: utf8
from fractions import Fraction
'''
В начале игры, они кладут несколько черных и белых жемчужин в одну коробку. На каждый ход, игрок берет жемчужину из 
коробки и кладет обратно жемчужину другого цвета. Побеждает тот, кто вытаскивает белую жемчужину на N-ом шаге.

Но Роботы не любят неопределенностей и предпочтут знать вероятность белой жемчужины на нужном шаге. Вероятность - это 
значение от 0 (0% шанс и что этого точно не будет) до 1 (100% шанс или это точно случится). Результат должен быть 
числом от 0 до 1 с точностью до 2-ого знака (±0.01).

Дана информация о начальном наборе жемчужин, как строка из "b" (черная) и "w" (белая) и количество итераций (N). 
Порядок жемчужин не важен.


Input: Стартовая последовательность жемчужин, как строк (str) и число итераций, как целое число (int).
Output: Вероятность вытащить белую жемчужину, как число (float).

Примеры:

checkio('bbw', 3) == 0.48
checkio('wwb', 3) == 0.52
checkio('www', 3) == 0.56
checkio('bbbb', 1) == 0
checkio('wwbb', 4) == 0.5
checkio('bwbwbwb', 5) == 0.48

Как это используется: В этой задаче вы можете потренироваться с основами теории вероятностей и статистики. И кстати, можете проверить, что независимо от начального состояния при возрастании количества итераций, вероятность будет стремиться к 0.5!

Предусловия: 0 < N ≤ 20
0 < len(pearls) ≤ 20
'''


def checkio(marbles, step):

    vse_hodi = [(marbles.count('b'), marbles.count('w'), 1)]    # Считаем кол-во чёрных / белых, вероятность 1
    znamenatelj = len(marbles)

    # Основной цикл
    for hod in range(step-1):
        new_vse_hodi = []
        for b, w, verojatnostj in vse_hodi:
            if b != 0:
                new_vse_hodi.append((b-1, w+1, Fraction(b, znamenatelj) * verojatnostj))
            if w != 0:
                new_vse_hodi.append((b + 1, w - 1, Fraction(w, znamenatelj) * verojatnostj))
        vse_hodi = new_vse_hodi

    result = 0

    # Цикл подсчёта вероятности по белым
    for b, w, verojatnostj in vse_hodi:
        result += Fraction(w, znamenatelj) * verojatnostj

    print(round(float(result), 2))
    print("*"*10)
    return round(float(result), 2)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    checkio('wbb', 3)
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
