'''
В этой миссии Ваша задача состоит в том, чтобы урезать предложение до длины, которая не превышает заданное количество символов.

Если данное предложение уже достаточно короткое, Вам не нужно ничего с ним делать. В случае, если его нужно урезать, отсутствующая часть должна быть обозначена присоединением многоточия ("...") к концу сокращенного предложения.

Сокращенное предложение может содержать целые слова и пробелы.
Оно не должно содержать ни усеченных слов, ни конечных пробелов.
Многоточие было учтено при расчете разрешенного количества символов, поэтому оно не засчитывается в счет заданной длины.

example

Входные данные: Два аргумента:

однострочное предложение в виде str;
максимальная длина усеченного предложения в виде int.
Выходные данные: Урезанное предложение с многоточием (если требуется) в виде одной строки.

Примеры:

assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

Предварительное условие:
line.startswith(' ') == False
0 < len(line) ≤ 79
0 < length ≤ 76
all(char in string.ascii_letters + ' ' for char in line)
'''


def cut_sentence(line: str, length: int) -> str:
    dots = '...'
    if len(line) <= length:
        return line

    words = line.split()
    cut_line = ""

    for word in words:
        if len(cut_line) + len(word) + 1 <= length:
            if cut_line:
                cut_line += " "
            cut_line += word
        else:
            break

    return cut_line + "..."


# These "asserts" are used for self-checking
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"
assert cut_sentence('Hi my name is Alex', 9) == 'Hi my...'

print("The mission is done! Click 'Check Solution' to earn rewards!")