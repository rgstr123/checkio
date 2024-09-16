'''
— Но я такой маленький! Зачем я тебе нужен?
— Послушай! Даже самый маленький воин может сделать армию намного сильнее, если он находится в нужном месте.
  И даже самый сильный может ослабить весь строй, если он встанет не в ту шеренгу.

Ваша задача — найти разность между наибольшим и наименьшим числами.
Эти числа могут быть получены соединением (конкатенацией) чисел данного массива.

Давайте рассмотрим пример. Если даны числа: 1, 2, 3, то 321 — это наибольшее число, а 123 — наименьшее.
Разность между этими числами — 198. Но, если даны числа: 4, 3 и 12, тогда 4312 — это наибольшее число, а 1234 — наименьшее.
Как видите, простой порядок — не то, что мы здесь ищем.

Входные данные: Список положительных целых чисел.
Выходные данные: Целое число.
'''


from typing import List


def bigger_together(ints: List[int]) -> int:
    """
        Returns difference between the largest and smallest values
        that can be obtained by concatenating the integers together.
    """
    # Преобразуем числа в строки для конкатенации
    str_ints = list(map(str, ints))

    # Сортировка для получения наименьшего числа
    smallest = ''.join(sorted(str_ints, key=lambda x: x * 10))

    # Сортировка для получения наибольшего числа
    largest = ''.join(sorted(str_ints, key=lambda x: x * 10, reverse=True))

    # Разница между наибольшим и наименьшим числом
    return int(largest) - int(smallest)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert bigger_together([1,2,3,4]) == 3087, "4321 - 1234"
    assert bigger_together([1,2,3,4, 11, 12]) == 32099877, "43212111 - 11112234"
    assert bigger_together([0, 1]) == 9, "10 - 01"
    assert bigger_together([100]) == 0, "100 - 100"
    assert bigger_together([3,12,22,32]) == 2099889, "3322212 - 1222323 = 2099889"
    print('Done! I feel like you good enough to click Check')