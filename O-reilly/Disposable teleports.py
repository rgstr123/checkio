import itertools
from collections import defaultdict


def checkio(teleports_string):

    # Записываем все порты в словарь
    ports_dict = defaultdict(set)
    for pair in teleports_string.split(","):
        ports_dict[pair[0]].add(pair[1])
        ports_dict[pair[1]].add(pair[0])
    print(ports_dict)

    # Рекурсивный метод поиска путей
    def recurse(at, visited, closed_ports):
        routes = available_routes(at, ports_dict, closed_ports)     # Ищем всех все пути(всех соседей) у текущей базы
        print(routes, at)
        if "1" in routes and len(visited) == 8:     # Возвращаем последнюю 1, если прошлись по всем базам (на этом заканчивается последняя рекурсия)
            return "1"
        for to in routes:                                               # Берём соседа
            new_used_routes = closed_ports | frozenset([(at, to)])      # Объединяем(записываем знач.) множество closed_ports (уже закрытых баз) с множеством (парой) текущей базы и соседа                  set.union(other, ...) или set | other | ...
            solution = recurse(to, visited | frozenset([to]), new_used_routes)  # Запускаем рекурсивный метод для соседа (идём к соседу) и добавляем его в visited
            if solution:
                print("solution", solution, to)
                return to + solution                                    # Возвращаем результат, причем в обратном порядке

    return "1" + recurse("1", frozenset("1"), frozenset())      # Возвращаем



def available_routes(from_, all_routes, used):
    is_used = lambda to: (from_, to) in used or (to, from_) in used
    return [to for to in all_routes[from_] if not is_used(to)]










# # Записываем все порты в словарь
#     teleports_list = [list(sorted([int(x), int(y)])) for x, y in teleports_string.split(",")]     # Не катит т.к. значения были int, а нужны str
#     ports_dict = {key: [] for key in list(itertools.chain.from_iterable(teleports_list))}         # Словарь, ключи - базы, знач. - все соседи. Это будет основная карта телепортов
#     for pair in teleports_list:
#         ports_dict[pair[0]].extend([pair[1]])
#         ports_dict[pair[1]].extend([pair[0]])
#
#
#
# # Метод ищет путь от любого порта до 1
# def find_path_to_1(ports, start, end=1, path=[]):
#     # print("Start:", start, "; End:", end)
#     path = path + [start]
#     if start == end:
#         return path
#     else:
#         if not start in ports:
#             return None
#         for node in ports[start]:
#             if node not in path:
#                 # print(node, path)
#                 newpath = find_path_to_1(ports, node, end, path)
#                 if newpath:
#                     return newpath
#         return None




###################################################################################################################
#
#                                                   Интересный вариант решения
#
# def checkio(string, length=8, start='1'):
#     def explore(edges, route):
#         node = route[-1]
#         print("node",node)
#         if node == start and len(set(route)) == length:
#             raise StopIteration(route)
#
#         for edge in (edge for edge in edges if node in edge):
#             print(edge)
#             print(edges)
#             explore(edges - {edge}, route + edge.replace(node, ''))
#
#     try: explore(set(string.split(',')), start)
#     except StopIteration as found: return found.value
###################################################################################################################



#################################################################################################################
#
#             Без рекурсии. Похож на мой первый вариант решения, но у меня до конца так и не получилось
#
#
# def checkio(teleports_string):
#     routes = defaultdict(list)
#     for route in teleports_string.split(','):
#         routes[route[0]].append(route[1])
#         routes[route[1]].append(route[0])
#
#     candidate = ['1' + s for s in routes['1']]
#
#     while True:
#         road = candidate.pop()
#         if road[-1] == '1' and len(set(road)) == 8:
#             return road
#         for next_route in routes[road[-1]]:
#             if next_route + road[-1] in road or road[-1] + next_route in road: continue
#             candidate.append(road + next_route)
##################################################################################################################


#This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"