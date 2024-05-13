'''

У Стефана есть друг -- маленькая робо-птичка. Какое-то время он пытался научить её говорить по-английски. И вот сегодня она произнесла первое слово: «hieeelalaooo». Звучит как «hello», но слишком уж много гласных. Стефан попросил Николу помочь с этим, и тот изучил, как птица меняет слова. Теперь нам осталось только написать модуль для перевода с птичьего.

Птичка меняет слова по следующим правилам:
- после каждой согласной буквы она добавляет случайную гласную букву (l ⇒ la or le);
- после каждой гласной буквы она добавляет две таких же буквы (a ⇒ aaa);
Гласные буквы == "aeiouy".
example

Вам дана птичья фраза как несколько слов, разделёных пробелами (каждая пара слов разделена одним пробелом). Птичка не знает ничего о знаках пунктуации и использует только буквы. Все слова даны в нижнем регистре. Необходимо перевести эту птичью песню в понятную простым роботам фразу.

Входные данные: Птичья фраза как строка (string).

Выходные данные: Перевод как строка (string).

Примеры:

assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"


Связь с реальной жизнью: Этот простой «шифр» похож на тот, который используют дети для своего «птичьего» языка.
Но теперь-то вы легко взломаете их хитрости.

Предусловия: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
Фраза всегда имеет перевод.
'''



VOWELS = "aeiouy"

def translate(phrase):

    phrase_list = list(phrase)
    for indx, char in enumerate(phrase_list):
        if char == " ":
            continue
        elif char in VOWELS:
            del(phrase_list[indx])
            del(phrase_list[indx])
        else:
            del(phrase_list[indx + 1])
    print("".join(phrase_list))
    return "".join(phrase_list)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
