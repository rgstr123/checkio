def checkio(n, m):

    trailing_len = max(len(bin(m))-2, len(bin(n))-2)
    n = format(n, '0{0}b'.format(trailing_len))
    m = format(m, '0{0}b'.format(trailing_len))
    return sum(i != j for i, j in zip(n, m))

#############################################################################
#                             Можно и так
#
# def checkio(n, m):
#     return str(bin(n ^ m)).count('1')
#############################################################################

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(999999, 1) == 11, "Third example"
