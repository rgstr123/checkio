# coding:utf8
from collections import defaultdict

def checkio(expression):
    for_check = ["(", ")", "{", "}", "[", "]"]
    bracket_dic = defaultdict(list)     # создаём словарь в котором значения листы
    express = list(expression)
    print("express", express)
    # res1 = False
    # res2 = False
    # res3 = False
    # if express.count(for_check[0]) == express.count(for_check[1]): res1 = True
    # elif express.count(for_check[2]) == express.count(for_check[3]): res2 = True
    # elif express.count(for_check[4]) == express.count(for_check[5]): res3 = True
    # else: pass
    #
    # if not res1 == res2 == res3: return False

    for item in for_check:
        print(bracket_dic)
        for count_item in expression:
            if item in express:
                bracket_dic[item].append(express.index(item))
                express[express.index(item)] = "."


    #TODO Осталось сделать: выбрать начальные к конечные скобки и проверить внутри них

    return

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
