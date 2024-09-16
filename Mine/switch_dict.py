'''
You are given a dictionary, where keys and values are strings.
Your function should return a dictionary as well, where keys and values from input dictionary are switched: input keys
become output values and vice versa. Looks easy? It is so! The only thing left to mention: the values in the result
dictionary should be sets (so the input key(s) - the element(s) of the set). Good luck!

Input: A dictionary.
Output: A dictionary.
'''


def switch_dict(data: dict[str, str]) -> dict[str, set]:
    result_dict = {}
    for key,value in data.items():
        if value not in result_dict:
            result_dict[value] = {key}
        if value in result_dict:
            result_dict[value].add(key)
    return result_dict


# These "asserts" are used for self-checking
assert switch_dict({"rouses": "red", "car": "red", "sky": "blue"}) == {
    "red": {"car", "rouses"},
    "blue": {"sky"},
}
assert switch_dict({"1": "one", "2": "two", "3": "one", "4": "two"}) == {
    "one": {"1", "3"},
    "two": {"2", "4"},
}
assert switch_dict({"a": "b", "b": "c", "c": "a"}) == {
    "b": {"a"},
    "c": {"b"},
    "a": {"c"},
}

print("The mission is done! Click 'Check Solution' to earn rewards!")