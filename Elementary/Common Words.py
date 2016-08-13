# coding: utf8

def checkio(first, second):

    first_1 = set(first.split(","))
    second_2 = set(second.split(","))

    return ",".join(sorted(first_1 & second_2))   # Можно писать и так:        first_1.intersection(second_2)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"