import operator
'''
This is a further development of Convert and Aggregate mission. You are given a list of tuples.
Each tuple consists of two values: a string and an integer.
You need to create and return a dictionary, where keys are string values (except the first character) from input tuples.
Values are aggregated integer values from input tuples for each specific key.
Each aggregating operation must be done according to the operation sign - the first character of string key.
Division by zero should be ignored. The resulted dictionary should not include items with empty key or zero value.

Input: List of tuples.
Output: Dictionary.

assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
assert aggr_operation([]) == {}
assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
assert aggr_operation([("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}
'''

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "=": (lambda x, y: y),
}


def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:
    result = {}

    for item in data:
        key = item[0][1:]
        value = item[1]
        op = item[0][0]
        division = True if item[0][0] == '/' else False
        operation = operations[item[0][0]]
        value = int(value)
        prev_value = int(result[key]) if result.get(key) else None

        if not all([division, value == 0]):
            if operation and not result.get(key) and operation(0, value) != 0 and key:
                result[key] = operation(0, value)
            elif operation and result.get(key) and key:
                result[key] = operation(prev_value, value)
                if operation(prev_value, value) == 0:
                    del result[key]
    return result

# These "asserts" are used for self-checking
assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
assert aggr_operation([]) == {}
assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
assert aggr_operation([("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}
assert aggr_operation([('+a', 0), ('*b', 0), ('+', 35)]) == {}
assert aggr_operation([('+a', 5), ('*a', 6), ('/a', 3), ('=a', 3)]) == {'a': 3}


print("The mission is done! Click 'Check Solution' to earn rewards!")