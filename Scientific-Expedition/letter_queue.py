'''
В области информационных технологий, очередь это структура данных с принципом доступа к элементам «первый
пришёл — первый вышел» (FIFO, First In — First Out). Добавление элемента (принято обозначать словом
"enqueue" — поставить в очередь или "push") возможно лишь в конец очереди, выборка — только из начала очереди
(что принято называть словом "dequeue" — убрать из очереди или "pop"), при этом выбранный элемент из очереди удаляется.
То есть чтобы добраться до нового добавленного элемента, нам надо "вытащить" элементы, которые были добавлены ранее.

Попробуем сделать модель очереди на Python. Вам дана последовательность команд:
- "PUSH X" -- поставить в очередь X, где X - это буква в верхнем регистре.
- "POP" -- убрать из начала очереди элемент. Если очередь пустая, то это команда ничего не делает.
Очередь содержит только буквы.

Вам необходимо обработать все команды и собрать все буквы, которые остались в очереди, в одно слово, от начала до конца очереди.

Рассмотрим пример. Дана последовательность команд:
["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]


Команда	    Очередь	    Примечания
________________________________________________________
PUSH A	    A	        Добавили "A" в пустую очередь
POP		                Убрали "A"
POP		                Очередь уже пуста
PUSH Z	    Z
PUSH D	    ZD
PUSH O	    ZDO
POP	DO
PUSH T	    DOT	        Результат


Входные данные: Последовательность команд, как список (list) строк (str).

Выходные данные: Содержание очереди, как строка (str).

Пример:

assert (
    letter_queue(
        ["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]
    )
    == "DOT"
)
assert letter_queue(["POP", "POP"]) == ""
assert letter_queue(["PUSH H", "PUSH I"]) == "HI"
assert letter_queue([]) == ""

Зачем это нужно: Очередь используется в информационных технологиях, транспорте и для обработки команд.
Очередь нужна, чтобы упорядочить данные и нагрузку поступающую одновременно.

Предусловия:
0 ≤ len(commands) ≤ 30;
all(re.match("\APUSH [A-Z]\Z", c) or re.match("\APOP\Z", c) for c in commands)
'''


def letter_queue(commands):
    queue = []

    for command in commands:
        if "PUSH" in command:
            queue.append(command[-1])
        else:
            if "POP" in command:
                if len(queue) == 0:
                    pass
                else:
                    queue.pop(0)
    print("".join(queue))
    return "".join(queue)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"