# coding: utf8
import itertools
'''
Подручные дроны Софии - это не какие-то тупые, бесчувственные железяки. Более того - они умеют дружить. На самом деле, они уже даже делают свою социальную сеть, только для дронов! София вытащила оттуда данные о всех связях между дронами и теперь хочет изучить эти взаимосвязи подробнее.
Дан массив прямых связей между дронами - кто с кем дружит. Каждая такая связь представлена, как строка с двумя именами разделеными дефисом. Для примера: "dr101-mr99" означает что dr101 и mr99 дружат между собой. Кроме этого даны два имени. Попробуйте определить, связаны ли они через других дронов, вне зависимости от глубины этих связей. Для примера: Если у двух дронов есть общий друг или друзья, у которых есть общий друг и так далее.

Давайте рассмотрим примеры:
scout2 и scout3 оба дружат с scout1 , так что они связаны. super и scout2 связаны между собой через sscout , scout4 и scout1 . Но вот dr101 и sscout никак не взаимосвязаны друг с другом.
Ввод: Три аргумента: информация о друзьях, как кортеж (tuple) строк (str); первое имя, как строка (str); второе имя, как строка (str).
Вывод: Связаны ли указанные дроны между собой, как булево значение (bool).

Примеры:
check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3") == True
check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout") == False
    
Связь с реальной жизнью: Данная идея может помочь вам в нахождении сложных взаимосвязей между событиями, которые на первый взгляд не имеют никакой связи. Ну и конечно узнаете немного о социальных сетях.

Предусловие: len(network) ≤ 45
если "name1-name2" в network , то "name2-name1" не в network
3 ≤ len(drone_name) ≤ 6
first_name и second_name всегда в network .
'''


def check_connection(network, first, second):

    pairs = [p.split("-") for p in network]

    graph = {key: [] for key in list(itertools.chain.from_iterable(pairs))}
    # Build a graph with all the pairs
    for pair in pairs:
        graph[pair[0]].extend([pair[1]])
        graph[pair[1]].extend([pair[0]])

    # now check if 'second' is linked to 'first'
    return find_path(graph, first, second) != None


def find_path(graph, start, end, path=[]):
    print("Start:", start, "; End:", end)
    path = path + [start]
    if start == end:
        return path
    else:
        if not start in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath:
                    return newpath
        return None


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
