# coding utf8
'''
Крестики и Нолики - это игра для двух игроков (Х и О), которые расставляют эти знаки на 3х3 поле. Игрок, который сумел
разместить три своих знака в любой горизонтали, вертикали или диагонали -- выигрывает.
Но сейчас мы не будем играть в эту игру. Вы будете судить игру, и оценивать результат. Вам дан результат игры, и вы
должны решить, кто победил или что это ничья. Ваша функция должна вернуть "X" если победил Х-игрок и "О" если победил
О-игрок. В случае ничьи, результат должен быть "D".

x-o-referee

Результаты игры представлены, как список строк, где "X" и "O" - это отметки игроков и "." - это пустая клетка.
Вх. данные: Результат игры, как список строк (unicode).
Вых. данные: "X", "O" или "D", как строка.

Примеры:

assert checkio(["X.O", "XX.", "XOO"]) == "X"
assert checkio(["OO.", "XOX", "XOX"]) == "O"
assert checkio(["OOX", "XXO", "OXX"]) == "D"
assert checkio(["O.X", "XX.", "XOO"]) == "X"

Как это используется: Эта задача поможет вам лучше понять, как работать с матрицами и вложеными массивами. Ну и конечно,
это будет полезно при разработке игр, так как надо уметь оценивать результаты.

Предусловия:

в играх может быть только один победитель или ничья;
len(game_result) == 3;
all(len(row) == 3 for row in game_result).
'''


def checkio(game_result):
    def check_rows(field):
        res = []
        for row in field:
            if row[0] == row[1] == row[2] and row[0] != ".":
                res.append(row[0])
            else:
                res.append("0")
        return res

    # Checking rows
    res_rows = check_rows(game_result)

    # Checking colums
    rotated_field = zip(*game_result)
    res_columns = check_rows(rotated_field)

    # Checking verticals
    if (game_result[0][0] == game_result[1][1] == game_result[2][2]):
        res_verticals = [game_result[0][0]]
    elif (game_result[0][2] == game_result[1][1] == game_result[2][0]):
        res_verticals = [game_result[0][2]]
    else:
        res_verticals = [0]

    # Preparation for results
    result_list = [res_rows, res_verticals, res_columns]
    x = 0
    o = 0
    for sums in result_list:
        x += sums.count("X")
        o += sums.count("O")

    # Results
    if x > 0 and o == 0:
        result = "X"
    elif o > 0 and x == 0:
        result = "O"
    else:
        result = "D"

    print("Result list: ", result_list)
    print("Count x: ", x)
    print("Count o: ", o)
    print("rows: ", res_rows)
    print("columns: ", res_columns)
    print("Vertical:  ", res_verticals)
    print("RESULT: ", result)
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"