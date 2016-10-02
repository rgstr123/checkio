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
