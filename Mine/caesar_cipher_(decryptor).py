'''
Эта миссия является частью набора задач. Другая задача - Caesar cipher encryptor .

О, нет! При получении зашифрованного сообщения мы обнаружили там лишние символы!
Ваша миссия - расшифровать текст сообщения (который будет состоять из букв только в нижнем регистре,
пробелов и специальных символов вроде "!", "&", "?") используя шифр Цезаря где каждая буква исходного текста
заменяется другой, которая находится на определенном расстоянии в алфавите. Например, ("a b c", 3) == "d e f"
Также вам нужно будет игнорировать/удалить все специальные символы. Таким образом сообщение вида ("!d! [e] &f*", -3)
будет расшифровано всего лишь как "a b c", не более.


Входные данные: Секретное сообщение как строка (только маленькие буквы, пробелы и специальные символы)
Output: Расшифрованный текст

Примеры:
to_decrypt("!d! [e] &f*", -3) == "a b c"
to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"

Как это используется: В криптографии, для сохранения важной информации, для сохранения секретности переписки.
'''


def to_decrypt(cryptotext, delta):
    result = ""

    for char in cryptotext:
        if char.isalpha():  # Если это буква
            # Применяем смещение по шифру Цезаря
            new_char = chr(((ord(char) - ord('a') + delta) % 26) + ord('a'))
            result += new_char
        elif char == ' ':  # Оставляем пробелы
            result += " "
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert to_decrypt("!d! [e] &f*", -3) == "a b c"
    assert to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
    assert to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
    assert to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
    assert to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"
    print("Coding complete? Click 'Check' to earn cool rewards!")