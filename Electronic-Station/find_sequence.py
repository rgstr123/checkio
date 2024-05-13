# coding: utf8
import re
"""
“There’s nothing here...” sighed Nikola.
“You’re kidding right? All treasure is buried treasure! It wouldn’t be treasure otherwise!” Said
Sofia. “Here, take these.” She produced three shovels from a backpack that seemed to appear out of thin air.
“Where did you get-”
“Don’t ask questions. Just dig!” She hopped on the shovel and began digging furiously.
CLUNK
“Hey we hit something.” Stephen exclaimed in surprise.
“It’s the treasure!” Sofia was jumping up and down in excitement.
The trio dug around the treasure chest and pulled it out of the hole and wiped the dirt off. Sofia tried grabbing the 
lid but it was locked. Nikola studied the locking mechanism.
“I’ve seen this type of lock before. It’s pretty simple. We just need to check whether there is a sequence of 4 or more 
matching numbers and output a bool.”
“Easy enough. Let’s open this sucker up!” Sofia was shaking in excitement.

Дана квадратная матрица размера NxN (4≤N≤10). Необходимо проверить есть ли здесь последовательность 4 или более 
одинаковых цифр. Последовательность должна неразрывно располагаться горизонтально, вертикально или по диагоналям 
(основным и дополнительным).

find-sequence
Входные данные: Матрица, как список (list) списков с целыми числами.

Выходные данные: Есть ли здесь последовательность, как булево значение (bool).

Примеры:

assert checkio([[1, 2, 1, 1], [1, 1, 4, 1], [1, 3, 1, 6], [1, 7, 2, 5]]) == True
assert checkio([[7, 1, 4, 1], [1, 2, 5, 2], [3, 4, 1, 3], [1, 1, 8, 1]]) == False
assert (
    checkio(
        [
            [2, 1, 1, 6, 1],
            [1, 3, 2, 1, 1],
            [4, 1, 1, 3, 1],
            [5, 5, 5, 5, 5],
            [1, 1, 3, 1, 1],
        ]
    )
    == True
)
assert (
    checkio(
        [
            [7, 1, 1, 8, 1, 1],
            [1, 1, 7, 3, 1, 5],
            [2, 3, 1, 2, 5, 1],
            [1, 1, 1, 5, 1, 4],
            [4, 6, 5, 1, 3, 1],
            [1, 1, 9, 1, 2, 1],
        ]
    )
    == True
)

Зачем это нужно: Эта концепция может пригодится в играх, которые используют последовательности элементов (вроде match3). А также для распознания образов.

Предусловия:

0 ≤ len(matrix) ≤ 10;
all(all(0 < x < 10 for x in row) for row in matrix).
"""


def checkio(matrix):

    def check_rows(matrix):  # Метод конвертирует числа в строку и ищет 4 одинаковые цифры
        result = False
        for row in matrix:
            if result:
                return result
            else:
                string_row = ""
                for y in row:
                    string_row += str(y)
                re_string = re.search(r'(\d)\1\1\1', string_row)
                if re_string:
                    result = True
        return result

    # Проверяем массив на длину
    if len(matrix) < 4: return False

    # Записываем в список все диагонали
    diag_right = []
    diag_left = []
    offset = -len(matrix)
    for diag in range(len(matrix)*2):
        diag_right.append([row[i + offset] for i, row in enumerate(matrix) if 0 <= i + offset < len(row)])
        diag_left.append([row[-i - 1 + offset] for i, row in enumerate(matrix) if 0 <= i - offset < len(row)])
        offset += 1

    # Проверяем на наличие 4 одинаковых цифр по всем напрвлениям
    checking_rows = check_rows(matrix)
    checking_columns = check_rows(zip(*matrix))     # zip возвращает кортеж, если нужен список, то   rotated = list(map(list, zip(*reversed(matrix))))
    checking_diag_right = check_rows(diag_right)
    checking_diag_left = check_rows(diag_left)

    # Если есть хоть одно совпадение, возвращаем True
    if any([checking_rows, checking_columns, checking_diag_right, checking_diag_left]): return True
    else: return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    assert checkio([[1, 9, 7, 8, 9, 3, 6, 5, 6, 2],
                    [4, 9, 4, 8, 3, 4, 8, 8, 5, 9],
                    [2, 8, 5, 5, 7, 8, 6, 1, 3, 6],
                    [6, 4, 7, 6, 9, 1, 4, 5, 7, 8],
                    [4, 7, 7, 9, 8, 8, 8, 8, 4, 4],
                    [3, 7, 3, 2, 1, 9, 1, 8, 9, 1],
                    [4, 7, 2, 4, 8, 1, 2, 3, 6, 2],
                    [4, 4, 1, 3, 3, 3, 9, 2, 6, 7],
                    [8, 6, 1, 9, 3, 5, 8, 1, 7, 5],
                    [7, 3, 6, 5, 3, 6, 6, 4, 8, 2]
    ]) == True, "Vot blin"
