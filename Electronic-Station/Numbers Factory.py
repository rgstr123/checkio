def checkio(number):
    result, divider = '', 9
    while divider > 1:
        if number % divider != 0:
            divider -= 1
        else:
             result = str(divider) + result
             number /= divider
    return int(result) if number == 1 else 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    # assert checkio(21) == 37, "2nd example"
    # assert checkio(17) == 0, "3rd example"
    # assert checkio(33) == 0, "4th example"
    # assert checkio(3125) == 55555, "5th example"
    # assert checkio(9973) == 0, "6th example"