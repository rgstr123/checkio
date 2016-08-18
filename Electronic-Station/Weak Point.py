# coding: utf8

def weak_point(matrix):

    row_sum = []
    column_sum =[]

    # Записываем в списки суммы строк и столбцов
    for x, y in zip(matrix, list(zip(*matrix))):    # zip(*matrix) переворачивает массив, zip(array1, array2) позволяет проходиться по ним одновременно
        row_sum.append(sum(x))
        column_sum.append(sum(y))

    # Ищем инндекс минимального эллемента в отсортированном массиве
    index_min_row = row_sum.index(sorted(row_sum)[0])
    index_min_column = column_sum.index(sorted(column_sum)[0])

    return index_min_row, index_min_column


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
