# coding: utf8

def checkio(data):
    # replace this for solution

    result = False
    digit = False
    upper = False
    lower = False

    if len(data) >= 10:
        for char_in_data in data:
            if char_in_data.isdigit():
                digit = True
            elif char_in_data.isupper():
                upper = True
            elif char_in_data.islower():
                lower = True
    else:
        print("Lenght < 10")
        result = False

    if digit and upper and lower:
        result = True

    return result


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"