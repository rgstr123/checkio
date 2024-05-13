# coding: utf8
import re

'''
"Где умный человек прячет лист? В лесу. Но что если леса нет? ... Он выращивает лес и прячет его там."
                                                                            -- Гилберт Кит Честертон

Когда-нибудь пробовали отправить секретное сообщение кому-то не пользуясь услугами почты? Вы можете использовать газету, 
чтобы рассказать кому-то свой секрет. Даже если кто-то найдет ваше сообщение, легко отмахнуться и сказать что это 
паранойя и теория заговора. Один из самых простых способов спрятать ваше секретное сообщение это использовать заглавные 
буквы. Давайте найдем несколько таких секретных сообщений.

Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.

Например: текст = " H ow are you? E h, ok. L ow or L ower? O hhh.", если мы соберем все заглавные буквы, то получим 
сообщение "HELLO".

Входные данные: Текст как строка (юникод).

Выходные данные: Секретное сообщение как строка или пустая строка.

Пример:

find_message(('How are you? Eh, ok. Low or Lower? '
 'Ohhh.')) == 'HELLO'
find_message('hello world!') == ''
find_message('HELLO WORLD!!!') == 'HELLOWORLD'

Как это используется: Это простое упражнение по работе со строками: итерация, чтение и объединение.

Предусловие: 0 < len(text) ≤ 1000
all(ch in string.printable for ch in text)
'''


def find_message(text):
    result = "".join(re.findall(r'[A-Z]', text))
    return result

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"