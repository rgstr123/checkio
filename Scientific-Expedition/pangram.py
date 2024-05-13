# coding: utf8
import string

'''
Панграмма (Греческий:παν γράμμα, pan gramma, "каждая буква") или предложение состоящее из разных букв алфавита, 
используя каждую букву по крайней мере один раз. Возможно, вы знакомы с хорошо известными панграммами 
"Эй, жлоб! Где туз? Прячь юных съёмщиц в шкаф" или "Любя, съешь щипцы, — вздохнёт мэр, — кайф жгуч", 
"The quick brown fox jumps over the lazy dog".

example

Для этого задания, вы будете использовать латинский алфавит (A-Z). У вас есть текст с латинскими буквами и знаками 
препинания. Вы должны проверить является ли предложение панграммой или нет. Регистр не имеет значения.

Входные данные: Текст как строка.

Выходные данные: Является предложение панграммой или нет как логическое.

Примеры:

assert check_pangram("The quick brown fox jumps over the lazy dog.") == True
assert check_pangram("ABCDEF") == False
assert check_pangram("abcdefghijklmnopqrstuvwxyz") == True
assert check_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True

Как это используется: Панграммы используют для отображения шрифтов, тестирования оборудования, развития почерка, 
каллиграфии и набора текста на клавиатуре.

Предусловия:

all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text);
0 < len(text).
'''


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
