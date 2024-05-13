# coding:utf8
"""
Дано выражение с цифрами, скобками и операторами. В данной задаче важны только скобки. Скобки представлены в трех
вариациях: "{}" "()" и "[]". Скобки используются, чтобы определить порядок применения операторов или ограничить участок
 выражения. Если скобка открывается, то она должна закрываться скобкой того же типа. Участки ограниченные одной парой
 скобок, не должны пересекаться с участками других скобок. В этой задаче, вам необходимо определить правильное ли
 выражение или нет, основываясь на расположении скобок. И не обращайте внимание на операторы и операнды.

Входные данные: Выражение для проверки, как строка (str, unicode).

Выходные данные: Решение, правильное выражение или нет, как булево значение (True или False).

Примеры:

assert checkio("((5+3)*2+1)") == True
assert checkio("{[(3+1)+2]+}") == True
assert checkio("(3+{1-1)}") == False
assert checkio("[1+1]+(2*2)-{3/3}") == True

Зачем это надо: Когда вы пишите большие формулы в вашем любимой математической программе. то лишняя или пропущеная скобка может превратится в очень сильную головную боль. И вот здесь то и необходим данный концепт, который используется во многих IDE.

Предусловия:
Выражение содержит только скобки ("{}" "()" or "[]"), цифры и/или операторы ("+" "-" "*" "/").
0 < len(expression) < 103
"""


def checkio(expression):
    print(expression)

    brackets = {'(': ')', '[': ']', '{': '}'}  # Основной словарь
    valid = [item for items in brackets.items() for item in items] # Список допустимых скобок

    # Перевернутый словарь нужен для доступа к ключам основного словаря, как к значениям (для описания ошибки)
    reverse = dict((value, key) for key, value in brackets.items())

    lastopened = []
    status = True


    def check(char):
        # Если открывающаяся скобка, то добавляем её в список
        if char in brackets.keys():
            lastopened.append(char)

        # Если закрывающаяся скобка
        else:
            # Убедимся, что была открывающаяся
            if len(lastopened) < 1:
                print('Закрывающая скобка ' + char + ' была до открывающей ' + reverse[char])
                nonlocal status
                status = False
            else:
                # Убедимся, что закрывающая скобка и открывающая совпадают
                if char != brackets[lastopened[-1]]:
                    status = False
                    print('Должна была быть такая ' + brackets[lastopened[-1]] + ' закрывающая скобка, но такая ' + char + ' встретилась раньше')

                # Если пара скобок была правильно закрыта, то удаляем из списка последнюю открывающую
                else:
                    print("Убираю ", lastopened[-1])
                    lastopened.pop()


    for char in range(len(expression)):
        if expression[char] in valid:
            check(expression[char])

    if len(lastopened) > 0:
        status = False
        print("Не было закрытия скобки " + brackets[lastopened[-1]])
    else:
        if status:
            print("Все скобки зактрыты правильно")
    print(status)
    print("-"*50)
    return status


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("({[3]})-[4/(3*{1001-1000}*3)/4]") == True, "MUST BE TRUE"
