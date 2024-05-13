# codding: utf8
import re

'''
Наши Роботы никогда не упускают возможности, чтобы улучшить свои навыки в лингвистике. Сейчас они изучают английский 
алфавит и что с этим делать.

Алфавит разделен на гласные и согласные буквы (Да, мы разделили буквы, а не звуки).
Гласные -- A E I O U Y
Согласные -- B C D F G H J K L M N P Q R S T V W X Z

Дан текст с разными словами и/или числами, которые разделены пробелами и знаками пунктуации. Числа не считаются за 
слова (также как и смесь букв и цифр). Необходимо подсчитать слова, в которых гласные буквы чередуются с согласными 
(полосатые слова), то есть в таких словах нет двух гласных или двух согласных букв подряд. Слова состоящие из одной 
буквы - не "полосатые" (не считайте их). Регистр букв не имеет значения.

Входные данные: Текст, как строка (str).

Выходные данные: Количество "полосатых" слов, как целое число (int).

Примеры:

assert checkio("My name is ...") == 3
assert checkio("Hello world") == 0
assert checkio("A quantity of striped words.") == 1
assert checkio("Dog,cat,mouse,bird.Human.") == 3

Зачем это нужно: Концепции используемые в данной задаче могут быть полезным упражнением для лингвистического анализа. 
Обработка текста - это очень важный инструмент для анализа книг и языков.

Предусловия:Текст содержит только ASCII символы.
0 < len(text) < 105
'''

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):

    words_list = re.split('\W+', text.upper())      # Либо text.upper()
    pattern = '^['+VOWELS+']?(['+CONSONANTS+']['+VOWELS+'])*['+CONSONANTS+']?$'

    count = 0

    for word in words_list:
        if len(word) <= 1:
            continue
        if re.match(pattern, word):    # Либо re.match(pattern, word, re.I)
            print(re.match(pattern, word))
            count += 1

    return count


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"