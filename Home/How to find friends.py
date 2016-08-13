# coding: utf8

import itertools


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
    #These "asserts" using only for self-checking and not necessary for auto-testing
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
