# coding: utf8
import re
'''
Теорема о бесконечных обезьянах утверждает, что абстрактная обезьяна, ударяя случайным образом по клавишам пишущей 
машинки в течение неограниченно долгого времени, рано или поздно напечатает любой наперёд заданный текст, например, 
полное собрание сочинений Джона Уоллиса (хотя вероятнее какой-нибудь из романов Дэна Брауна).
Предположим, что наши обезьяны печатают, и печатают, и печатают, и уже настрочили множество разнообразных коротких 
отрывков текста. Давайте проверим их на вхождение осмысленных слов.
Вам предлагается некоторый текст, который может содержать осмысленные слова. Вы должны подсчитать количество таких 
слов в этом тексте. Слово может стоять отдельно, а может присутствовать как часть другого слова. Регистр букв не имеет 
значения. Слова даны в нижнем регистре и не повторяются. Если слово встречается в тексте несколько раз, оно должно быть 
посчитано только один раз.
Например, текст "How aresjfhdskfhskd you?", слова - ("how", "are", "you", "hello"). Результат должен быть равен 3.
Вход: Два аргумента. Текст как строка (юникод в Python 2) и слова в виде множества (set) строк (юникод в Python 2).
Выход: Количество слов в тексте в виде целого числа.

Пример:

count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {"sum", "hamlet", "infinity", "anything"}) == 1

Как это используется: Python удобный и мощный язык для обработки текстовых данных. В этой задаче приводится всего лишь 
простой пример инструментов для поиска в тексте, которые вы можете разрабатывать.

Предусловия:
0 < len(text) ≤ 256
all(3 ≤ len(w) and w.islower() and w.isalpha for w in words)
'''


def count_words(text, words):

    count = 0
    words_copy = list(words)
    for x in words_copy:
        if re.findall(x, text.lower()):
            count += 1
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"