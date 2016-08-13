# coding: utf8


def checkio(number):
    num = bin(number)
    print("Number ", number, " in binary is: ", num)
    count = num.count("1")
    print("1 count: ", count)
    return count



# ____________________________________________________________________________
#
#     Быстрая запись:
#
#     return bin(number).count("1")
#
#
# ____________________________________________________________________________


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9