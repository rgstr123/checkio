'''
The Robots have found an encrypted message. We cannot decrypt it right now, but we can take the first steps.
Given a set of "words," (for simplicity we will use lowercase latin letters as symbols) each word contains symbols at
the "alphabetical" order (It is not in the latin alphabetical order, but a different order). We need to determine the
order of all the symbols from each word and create one word with all the symbols at once from given words in the
"alphabetical" order. For some cases, if we can not determine the order for several symbols -- use latin alphabetical
order. For example: Given words "acb", "bd", "zwa". As we can see "z" and "w" must be before "a" and "d" after "b".
So the result is "zwacbd".

Precondition: In each test, there will be only one solution.

Input: A list of strings.

Output: A string.

Example:

checkio(["acb", "bd", "zwa"]) == "zwacbd"
checkio(["klm", "kadl", "lsm"]) == "kadlsm"
checkio(["a", "b", "c"]) == "abc"
checkio(["aazzss"]) == "azs"
checkio(["dfg", "frt", "tyg"]) == "dfrtyg"
'''

def checkio(data):
    syms = set()
    rulesSmaller = {}

    for word in data:
        for sym in word:
            syms.add(sym)
    print("syms:            ", syms)

    # Заполняем словарь значениями
    for sym in syms:
        rulesSmaller.setdefault(sym, set())
    print("rullerSmaller:   ", rulesSmaller)

    # TODO думаю надо сделать когда буквы идут ПОСЛЕ (пересмотреть весь код)
    # Заполняем словарь: ключ = буква, значение = буквы которые в новом алфавите идут ПЕРЕД буквой (в ключе)
    for word in data:
        for i in range(len(word) - 1):
            if word[i] != word[i + 1]:
                rulesSmaller[word[i + 1]].add(word[i])
    print("rullerSmaller:   ", rulesSmaller)

    # Сюда попадают неопределённые буквы (буквы перед которыми мы не знаем). С них будем начинать поиск (в новом алфавите они будут стоять первыми)
    parts = []
    for sym in syms:
        if len(rulesSmaller[sym]) == 0:
            parts.append(sym)
    print("parts:           ", parts)

    visited = []
    while len(visited) != len(syms):
        while len(parts) != 0:
            # из неопределённых букв выбираем наименьшую по латинскому алфавиту (из условия)
            now = min(parts)
            visited.append(now)
            parts.remove(now)

            for i in rulesSmaller:
                if now in rulesSmaller[i]:
                    rulesSmaller[i].remove(now)
            print("visited:   ", visited)
        for i in [x for x in syms if x not in visited]:
            print(i)
            if len(rulesSmaller[i]) == 0:
                parts.append(i)

    return ''.join(visited)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
    #     "Just concatenate it"
    # assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
    #     "Paste in"
    # assert checkio(["a", "b", "c"]) == "abc", \
    #     "Cant determine the order - use english alphabet"
    # assert checkio(["aazzss"]) == "azs", \
    #     "Each symbol only once"
    # assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
    #     "Concatenate and paste in"
    # assert checkio(["axton","bxton"]) == "abxton", \
    #     "Заваливается через раз на этом тесте"
    # assert checkio(["bxton","dxton"]) == "bdxton", \
    #     "Заваливается через раз на этом тесте"
    assert checkio(["ghi","abc","def"]) == "abcdefghi", \
        "Тоже не проходит"