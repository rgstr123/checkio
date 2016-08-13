# coding utf8

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