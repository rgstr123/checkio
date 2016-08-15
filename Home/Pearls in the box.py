# coding: utf8
from fractions import Fraction


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
