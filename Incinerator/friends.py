# coding: uft8
'''
В задании "Как найти друзей" ("How to find friends") , было бы удобно работать, используя специальную структуру данных. В этом задании мы разработаем структуру данных, которую будем применять для хранения и обработки социальной сети.
Класс "Friends" должен содержать данные о людях (их имена) и о связях между ними. Имена представлены в виде текстовых строк, чувствительных к регистру. Связи не имеют направлений, то есть, если существует связь "sofia" с "nikola", это справедливо и в обратную сторону.

class Friends (connections)
Возвращает новый объект, экземпляр класса Friends. Параметр "connections" имеет тип "итерируемый объект", содержащий множества (set) с двумя элементами в каждом. Каждая связь содержит два имени в виде текстовых строк. Связи могут повторяться в параметре инициализации, но в объекте хранятся только уникальные пары. Каждая связь имеет только два состояния - присутствует или не присутствует.

>>> Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"})
>>> Friends([{"1", "2"}, {"3", "1"}])

add (connection)
Добавляет связь в объект. Параметр "connection" является множеством (set) из двух имен (строк). Возвращает True, если заданная связь новая и не присутствует в объекте. Возвращает False, если заданная связь уже существует в объекте.

>>> f = Friends([{"1", "2"}, {"3", "1"}])
>>> f.add({"1", "3"})
False
>>> f.add({"4", "5"})
True

remove (connection)
Удаляет связь из объекта. Параметр "connection" является множеством (set) из двух имен (строк). Возвращает True, если заданная связь существует в объекте. Возвращает False, если заданная связь не присутствует в объекте.

>>> f = Friends([{"1", "2"}, {"3", "1"}])
>>> f.remove({"1", "3"})
True
>>> f.remove({"4", "5"})
False

names ()
Возвращает множество (set) имён. Множество содержит имена, которые имеют хотя бы одну связь.

>>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"})
>>> f.names()
{"a", "b", "c", "d"}
>>> f.remove({"d", "c"})
True
>>> f.names()
{"a", "b", "c"}

connected (name)
Возвращает множество (set) имён, которые связаны с именем, заданным параметром "name" . Если "name" не присутствует в объекте, возвращается пустое множество (set).

>>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"})
>>> f.connected("a")
{"b", "c"}
>>> f.connected("d")
set()
>>> f.remove({"c", "a"})
True
>>> f.connected("c")
set()

В этом задании все входные данные корректны, и выполнять их проверку не обязательно.
Входные данные: Операторы и выражения с классом Friends.
Выходные данные: Поведение объекта, как описано выше.
Как это используется: Здесь вы реализуете класс с изменяемым состоянием. Это не простая структура данных с несколькими методами, а реализация более сложного объекта.
Предусловие: Все данные корректны.
'''


class Friends:
    def __init__(self, connections):

        self.connections = connections
        self.connections = list(self.connections) # Perevozhu v list, 4to bi leg4e bilo udaljat' dobavljat' elementi

    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            self.connections.append(connection)
            return True


    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False

    def names(self):
        all_names = set()
        for x, y in self.connections:
            all_names.add(x)
            all_names.add(y)
        return all_names

    def connected(self, name):
        connection_list = set()
        for x, y in self.connections:
            if x == name:
                connection_list.add(y)
            if y == name:
                connection_list.add(x)
        return connection_list



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"