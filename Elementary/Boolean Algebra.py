# coding: utf8

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if operation == OPERATION_NAMES[0] and x and y: return 1
    if operation == OPERATION_NAMES[1] and (x or y): return 1
    if operation == OPERATION_NAMES[2] and (not x or y): return 1
    if operation == OPERATION_NAMES[3] and x != y: return 1
    if operation == OPERATION_NAMES[4] and x == y: return 1
    return 0



# _______________________________________________________________________________
#                         МОЖНО ЧЕРЕЗ ЛЯМБДУ
#
#
# funcs = {"conjunction": lambda x, y: x & y,
#          "disjunction": lambda x, y: x | y,
#          "implication": lambda x, y: x <= y,
#          "exclusive"  : lambda x, y: x ^ y,
#          "equivalence": lambda x, y: x == y}
#
#
# def boolean(x, y, operation):
#     return funcs[operation](x, y)
#
#
# _______________________________________________________________________________


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"