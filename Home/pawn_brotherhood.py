# coding: utf8

'''
Сколько вам лет в днях? Это легко вычислить - достаточно вычесть свой день рождения от сегодняшнего дня. Мы имеем реальную задачу - посчитать разницу между любыми датами.
У вас есть две даты в кортежах с тремя числами - год, месяц и день. Например, 19 апреля 1982 будет (1982, 4, 19). Вы должны найти разницу в днях между имеющимися датами. Например, между сегодня и вчера = 1 день. Разница между днями всегда будет положительной или нулем, не забывайте про абсолютное значение.

Входные данные: Две даты, как кортежи целых чисел.
Выходные данные: Разница между датами в днях, как целое число.

Примеры:

assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238

Зачем это нужно: Python идет "в комплекте с батарейками", таким образом, вам полезно будет узнать, как использовать готовые модули, чтобы не изобретать велосипед снова и снова.

Предусловия:

даты между 1 января 1 и 31 декабря 9999;
даты корректны.
'''

def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))


def get_char(x):
    return str(''.join(ele for ele in x if ele.isalpha()))


def safe_pawns(pawns):
    positions = ["a", "b", "c", "d", "e", "f", "g", "h"]
    result_set = set()

    for pawn in pawns:
        charz = get_char(pawn)
        numz = get_num(pawn)
        if 0 < numz <= 7:
            if charz in positions and charz != "h" and charz != "a":
                tempC1 = positions.index(charz)-1
                tempC2 = positions.index(charz)+1
                tempN = numz+1
                temp1 = str(positions[tempC1]) + str(tempN)
                temp2 = str(positions[tempC2]) + str(tempN)
                if temp1 in pawns:
                    result_set.add(temp1)
                if temp2 in pawns:
                    result_set.add(temp2)
            elif charz == "a":
                tempNa = numz + 1
                tempa = "b" + str(tempNa)
                if tempa in pawns:
                    result_set.add(tempa)
            elif charz == "h":
                tempNh = numz + 1
                temph = "g" + str(tempNh)
                if temph in pawns:
                    result_set.add(temph)
            else:
                continue
    return len(result_set)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1