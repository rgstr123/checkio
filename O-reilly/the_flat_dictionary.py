# coding: utf8
'''
Никола обожает классифицировать все, что видит вокруг. Однажды Стефан подарил ему устройство для ярлыков на день
рождение, и затем они неделями отдирали наклейки со всех поверхностей и вещей на корабле. Он категоризировал все
реагенты в своей лаборатории, книги в библиотеке и даже заметки на столе. Но когда он узнал о том, что в Python
словари, он категоризировал все конфигурационные файлы дронов Софии. Теперь эти файлы организованы в сложную вложенную
структуру, что очень не нравится Софии. Помогите ей упростить эти словари словарей.
Словари - это удобный тип данных для хранения и обработки различных конфигураций. Они позволяют хранить данные по
ключам и создавать вложенные структуры. Дан словарь, в котором в качестве ключей используются строки, а в качестве
значений строки или словари. Необходимо сделать этот словарь "плоским", но сохранить структуру в ключах. Результатом
будет словарь без вложенных словарей. Ключи должны содержать путь, составленный из родительских ключей из начального
словаря, разделенных "/". Если значение ключа есть пустой словарь, тогда оно должно быть заменено пустой строкой ("").
Взглянем на пример:

{
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}
    }
}

Результатом будет:

{"name/first": "One",           # one parent
 "name/last": "Drone",
 "job": "scout",                # root key
 "recent": "",                  # empty dict
 "additional/place/zone": "1",  # third level
 "additional/place/cell": "2"}

Входные данные: Оригинальный словарь (dict).
Выходные данные: "Плоский" словарь (dict).

Примеры:

assert flatten({"key": "value"}) == {"key": "value"}
assert flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {
    "key/deeper/more/enough": "value"
}
assert flatten({"empty": {}}) == {"empty": ""}
assert flatten(
    {
        "name": {"first": "One", "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {"place": {"zone": "1", "cell": "2"}},
    }
) == {
    "name/first": "One",
    "name/last": "Drone",
    "job": "scout",
    "recent": "",
    "additional/place/zone": "1",
    "additional/place/cell": "2",
}

Связь с реальной жизнью: Методы из этой задачи будут полезны, чтобы разобрать и упростить структуры конфигураций или
файлов. Вы легко можете улучшить данную концепцию для ваших конкретных задач. А также, чтение чужого кода и поиск
ошибок - это очень полезный навык.

Предусловия:

ключи в словаре - не пустые строки;
значения в словаре - строки или другие словари;
root_dictionary != {}.
'''


def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if isinstance(v, dict): # Check if the value is a dictionary
                if v:               # If that value is NOT empty , it adds it to the stack and continue going deeper
                    stack.append((path + (k,), v))
                else:
                    result["/".join((path + (k,)))] = "" # If value is an empty dictionary, result() is appended with an empty str into the value
            else:
                result["/".join((path + (k,)))] = v # If value is not a dictionary? then result is appended with path and value
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}