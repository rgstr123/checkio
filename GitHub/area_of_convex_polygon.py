'''
Дан выпуклый многоугольник на координатной плоскости. Данный многоугольник представлен, как массив координат вершин.
Вершины соединены последовательно друг с другом и последняя в массиве соединена с первой. Многоугольник имеет N вершин.
Вам нужно написать программу для расчета площади многоугольника. Результат должен быть с точностью до одного знака или ±0.1.
Входные данные: Координаты, как список (list) списков. Каждый список содержит два целых числа.
Входные данные: Площадь многоугольника, как число.

Example:

checkio([[1, 1], [9, 9], [9, 1]]) == 32
checkio([[4, 10], [7, 1], [1, 4]]) == 22.5
checkio([[1, 2], [3, 8], [9, 8], [7, 1]]) == 40
checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]) == 26
checkio([[7, 2], [3, 2], [1, 5],
         [3, 9], [7, 9], [9, 6]]) == 42
checkio([[4, 1], [3, 4], [3, 7], [4, 8],
         [7, 9], [9, 6], [7, 1]]) == 35.5

Как это используется: Данная проблема часто стоит в топографии и архитектуре. Вы можете усовершенствовать этот алгоритм и подсчитать площадь любой выделенной зоны на карте. Ну или вам нужно будет построить что-то и рассчитать стройматериалы.

Предусловия: 3 ≤ N ≤ 8
∀ x, y ∈ coordinates : 0 ≤ x ≤ 10; 0 ≤ y ≤ 10;
'''


def checkio(data):
    # http://ru.wikihow.com/найти-площадь-многоугольника

    data = [data[0]] + data[::-1]
    x_y = 0
    y_x = 0
    for x1, y2 in zip(data, data[1:]):
        x_y += x1[0] * y2[1]
        y_x += x1[1] * y2[0]

    print(abs((x_y - y_x) / 2))
    return abs((x_y - y_x) / 2)


if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([[1, 1], [9, 9], [9, 1]]), 32), "The half of the square"
    assert almost_equal(checkio([[4, 10], [7, 1], [1, 4]]), 22.5), "Triangle"
    assert almost_equal(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]), 40), "Quadrilateral"
    assert almost_equal(checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]), 26), "Pentagon"
    assert almost_equal(checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]]), 42), "Hexagon"
    assert almost_equal(checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]), 35.5), "Heptagon"

