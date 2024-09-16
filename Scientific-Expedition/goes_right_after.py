'''
In a given word you need to check if one symbol goes only right after another.

Cases you should expect while solving this challenge:

one of the symbols is not in the given word - your function should return False;
any symbol appears in a word more than once - use only the first one;
two symbols are the same - your function should return False;
the condition is case sensitive, which means 'a' and 'A' are two different symbols.
example

Input: Three arguments. The first one is a given string (str), second is a symbol (str) that should go first, and the
third is a symbol (str) that should go after the first one.

Output: A logic value (bool).

Examples:

assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
'''


def goes_after(word: str, first: str, second: str) -> bool:
    if first not in word or second not in word: return False
    index_first = word.index(first)
    index_second = word.index(second)

    return True if first in word and \
        index_first < len(word)-1 and \
        first+second == word[index_first]+word[index_first+1] and \
        index_second == index_first+1 \
    else False


print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")