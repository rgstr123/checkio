'''
This function should take a string as an input and return the count of vowels (a, e, i, o, u) in the string.
The function should be case-insensitive.

Input: String (str).
Output: Integer (int).

Examples:

assert count_vowels("hello") == 2
assert count_vowels("openai") == 4
assert count_vowels("typescript") == 2
assert count_vowels("a") == 1

How it’s used:

in natural language processing tasks, like text analysis and statistics;
in text-based games or learning applications, for instance, to calculate the difficulty level of a word or phrase.
Preconditions:

text ∈ string;
length(text) >= 0.
'''


def count_vowels(text: str) -> int:
    VOWELS = "aeiou"
    count = 0

    for char in text.lower():
        if char in VOWELS:
            count += 1
    return count


# These "asserts" are used for self-checking
assert count_vowels("hello") == 2
assert count_vowels("openai") == 4
assert count_vowels("typescript") == 2
assert count_vowels("a") == 1
assert count_vowels("b") == 0
assert count_vowels("aeiou") == 5
assert count_vowels("AEIOU") == 5
assert count_vowels("The quick brown fox") == 5
assert count_vowels("Jumps over the lazy dog") == 6
assert count_vowels("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
