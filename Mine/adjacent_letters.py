'''
You are given a string, where all letters are of same case.
This string could include adjacent letters - two the same letters together ("aa", "bb" etc).
Your task in this mission is to remove both these letters. If after removing one pair a new appears - remove it as well!
Each such pair should be removed from string until no one remains. Good luck!

Input: String (str).
Output: String (str).
'''


def adjacent_letters(line: str) -> str:
    # Initialize an empty stack
    stack = []

    # Loop over each character in the input string
    for char in line:
        # If the stack is not empty and the last character is the same as the current one
        if stack and stack[-1] == char:
            # Remove the last character from the stack
            stack.pop()
        else:
            # Otherwise, add the current character to the stack
            stack.append(char)

    # Convert the stack back to a string and return
    return ''.join(stack)


# These "asserts" are used for self-checking
assert adjacent_letters("adjacent_letters") == "adjacent_lrs"
assert adjacent_letters("") == ""
assert adjacent_letters("aaa") == "a"
assert adjacent_letters("ABBA") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
