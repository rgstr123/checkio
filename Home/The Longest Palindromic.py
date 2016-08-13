def longest_palindromic(text):          # Скопировал с инета. Сам не смог решить
    result = ""
    for i in range(len(text)):      # Тут просто перебираем числа длины текста
        for j in range(i,-1,-1):    # Тут делаем ОБРАТНЫЙ список из числа i до -1 (не вкл.), с шагом -1. (например i=2, тогда список: 2, 1, 0)
            # result = текущему тексту (от j до i+1) если текущий текст == себе же перевёрнутому и пред. результаты были меньше по длине
            # иначе результат остаётся каким был
            result = text[j:i + 1] if text[j:i + 1] == text[j:i + 1][::-1] and len(result) < len(text[j:i + 1]) else result
    return result


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"