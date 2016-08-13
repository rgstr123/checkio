# coding: utf8


def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))


def get_char(x):
    return str(''.join(ele for ele in x if ele.isalpha()))


def safe_pawns(pawns):
    possitions = ["a", "b", "c", "d", "e", "f", "g", "h"]
    result_set = set()

    for a in pawns:
        charz = get_char(a)
        numz = get_num(a)
        if 0 < numz <= 7:
            if charz in possitions and charz != "h" and charz != "a":
                tempC1 = possitions.index(charz)-1
                tempC2 = possitions.index(charz)+1
                tempN = numz+1
                temp1 = str(possitions[tempC1]) + str(tempN)
                temp2 = str(possitions[tempC2]) + str(tempN)
                if temp1 in pawns:
                    result_set.add(temp1)
                if temp2 in pawns:
                    result_set.add(temp2)
            elif charz == "a":
                tempNa = numz + 1
                tempa = "b" + str(tempNa)
                if tempa in pawns:
                    result_set.add(tempa)
            elif charz == "h":
                tempNh = numz + 1
                temph = "g" + str(tempNh)
                if temph in pawns:
                    result_set.add(temph)
            else:
                continue
    return len(result_set)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1