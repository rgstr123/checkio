# coding: utf8

import string


def check_pangram(text):
    list_alpha = list(string.ascii_lowercase)
    list_text = list(text.lower())

    for x in list_text:
        if x in list_alpha:
            list_alpha.pop(list_alpha.index(x))

    if len(list_alpha) == 0:
        return True
    else:
        return False

# ___________________________________________________________________________
# Можно было сделать наоборот, пройтись циклом по всем буквам алфавита и
# проверять есть ли они в ТЕКСТЕ, если нет то False. Например так:
#
# def check_pangram(text):
#     from string import ascii_lowercase
#     for i in ascii_lowercase:
#         if not i in text.lower() and i.isalpha():
#             return False
#     return True
#
# ___________________________________________________________________________


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
