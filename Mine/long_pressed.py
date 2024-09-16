'''
Sometimes your friends want to express their feelings in a message, and sometimes a key with a letter gets stuck on the keyboard.
In both cases we will get a "long-pressed letter" and the letter will then be printed more than once.
You are given two strings. The first string is the original text message.
The second string is a printed message, which may contain several (or possibly none) long-pressed letters.
It may happen that the message was written in a hurry, so do not forget to check that all the letters match those in the original.
Return True if the printed message matches the original one, taking into account possible long keystrokes.
Or False if there are errors or no long-pressed letters.
'''


def long_pressed(text: str, typed: str) -> bool:
    i, j = 0, 0

    if text == typed:
        return False  # Returning False if there's an exact match
    i, j = 0, 0

    while j < len(typed):
        if i < len(text) and text[i] == typed[j]:
            i += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            pass
        else:
            return False
        j += 1

    return i == len(text)


print("Example:")
print(long_pressed("alex", "aaleex"))

# These "asserts" are used for self-checking
assert long_pressed("alex", "aaleex") == True
assert long_pressed("welcome to checkio", "weeeelcome to cccheckio") == True
assert long_pressed("there is an error here", "there is an errorrr hereaa") == False
assert long_pressed("hi, my name is...", "hi, my name is...") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")