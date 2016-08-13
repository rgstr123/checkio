# coding: utf8
import re


def checkio(text):
    # replace this for solution

    result_dict = {}
    text = text.lower()
    text_re = re.findall(r'[a-z]', text)

    for chars in text_re:
        a = text_re.count(chars)
        b = chars

        result_dict[b] = a

    max_value = max(result_dict.values())
    keys = [x for x, y in result_dict.items() if y == max_value]
    keys = sorted(keys)

    return keys[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
