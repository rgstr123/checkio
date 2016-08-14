# codding: utf8
import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):

    words_list = re.split('\W+', text.upper())      # Либо text.upper()
    pattern = '^['+VOWELS+']?(['+CONSONANTS+']['+VOWELS+'])*['+CONSONANTS+']?$'

    count = 0

    for word in words_list:
        if len(word) <= 1:
            continue
        if re.match(pattern, word):                 # Либо re.match(pattern, word, re.I)
            print(re.match(pattern, word))
            count += 1

    return count



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"