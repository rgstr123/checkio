import itertools

def RemoveDups(ListObject):
    temp = list(set(ListObject))
    temp.sort(key=lambda x: ListObject.index(x))
    return temp

def encode(message, secret_alphabet, keyword):
    message = message.lower().replace(" ", "")

    table = {key: val for key, val in zip(secret_alphabet, itertools.product(["A", "D", "F", "G", "V", "X"], repeat=2))}
    # test = {key: [val] for key in secret_alphabet for val in itertools.product(["A", "D", "F", "G", "V", "X"], repeat=2)}

    encr_message = ""
    for char in message:
        if char in secret_alphabet:
            for x in table.get(char):
                encr_message += x

    keyword = RemoveDups(keyword)
    HeadingTable = {}
    counter = 0
    for i in itertools.cycle(keyword):
        if i not in HeadingTable:
            HeadingTable[i] = ''
        HeadingTable[i] += encr_message[counter]
        counter += 1
        if counter == len(encr_message):
            break
    print(''.join([HeadingTable[i] for i in sorted(HeadingTable.keys())]))
    return ''.join([HeadingTable[i] for i in sorted(HeadingTable.keys())])


def CreateHeadingTable(keyword, message):
    HeadingTable = {}
    for i in keyword:
        HeadingTable[i] = []

    counter = 0
    for i in itertools.cycle(keyword):
        HeadingTable[i].append('')
        counter += 1
        if counter == len(message):
            break

    for i in sorted(HeadingTable.keys()):
        HeadingTable[i] = list(message[:len(HeadingTable[i])])
        message = message[len(HeadingTable[i]):]
    return HeadingTable



def decode(message, secret_alphabet, keyword):
    keyword = RemoveDups(keyword)
    heading_table = CreateHeadingTable(keyword, message)

    encr_message = ""

    counter = 0
    for x in itertools.cycle(keyword):
        encr_message += heading_table[x][0]
        del heading_table[x][0]
        counter += 1
        if counter == len(message):
            break

    table = {key: val for key, val in zip( itertools.product(["A", "D", "F", "G", "V", "X"], repeat=2), secret_alphabet)}

    OriginalMessage = ""
    first_char = ""
    counter = 1
    for second_char in encr_message:
        if counter == 1:
            first_char = second_char
            counter += 1
        elif counter == 2:
            OriginalMessage += table[first_char, second_char]
            counter = 1

    print(OriginalMessage)
    return OriginalMessage


if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'attackat1200am', "decode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    assert decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"



############################## Интересное решение ##############################
#
# import re
# import itertools
# from collections import defaultdict
# import math
#
#
# def encode(message, secret_alphabet, keyword):
#     # Remove non-alphanumeric characters
#     message = re.sub('[^a-zA-Z0-9]', '', message).lower()
#     d = {}
#     # Create "adfgvx" table with our secret_alphabet
#     for i, p in enumerate(itertools.product('ADFGVX', repeat=2)):
#         d[secret_alphabet[i]] = ''.join(p)
#     # Convert message to fractionated form (row-column)
#     message = ''.join([d.get(i) for i in message])
#     # Remove duplicated letters from keyword
#     keyword = ''.join(sorted(set(keyword), key=keyword.index))
#     # Create a new table with a key as the heading
#     d = defaultdict(list)
#     for v, k in list(zip(keyword * len(message), message)):
#         d[v].append(k)
#     return ''.join([''.join(d[k]) for k in sorted(d)])
#
#
# def decode(message, secret_alphabet, keyword):
#     # Remove duplicated letters from keyword
#     keyword = ''.join(sorted(set(keyword), key=keyword.index))
#     fill_len = math.ceil(len(message) / len(keyword))
#     # Create a new table with a key as the heading
#     d = defaultdict(list)
#     for v, k in list(zip(keyword * len(message), message)):
#         d[v].append(k)
#     code_dict = {}
#     offset = 0
#     for k in sorted(d):
#         code_dict.update({k: message[offset: offset + len(''.join(d[k]))]})
#         offset += len(''.join(d[k]))
#     # "Allign" for matrix transformation
#     l_str = [code_dict.get(c) if len(code_dict.get(c)) == fill_len
#              else code_dict.get(c) + ('_' * fill_len) for c in keyword]
#     # Transform matrix
#     w = ''.join([''.join([y for y in x]).strip('_') for x in zip(*l_str)])
#     d = {}
#     # Create "adfgvx" table with our secret_alphabet
#     for i, p in enumerate(itertools.product('ADFGVX', repeat=2)):
#         d[''.join(p)] = secret_alphabet[i]
#     return ''.join([d.get(w[i:i + 2]) for i in range(0, len(w), 2)])