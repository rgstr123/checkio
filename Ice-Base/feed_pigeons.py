# coding: utf8
'''
Я начал кормить одного из голубей. Через минуту прилетело еще два, и еще через минуту прилетело еще три голубя. Затем 4
и так далее (Пр: 1+2+3+4+...). Одной порции корма хватает одному голубю на минуту. В случае если еды не хватает на всех
птиц, то сначала едят те голуби, что прилетели ранее. Голуби - это вечно голодные птицы и они будут есть и есть без
остановки. Если у меня есть N порций корма, то сколько голубей я смогу покормить хотя бы по разу?
Входные данные: Количество порций корма, как целое число (int).
Выходные данные: Количество накормленных голубей, как целое число (int).

Примеры:

assert checkio(1) == 1
assert checkio(3) == 2
assert checkio(5) == 3
assert checkio(10) == 6
1
2
3
4
Как это используется: В этой задаче мы видим, как можно использовать программирование для моделирования ситуаций. Конечно, любая модель имеет свои ограничения и приближения, но чаще всего нам и не нужна идеальная модель.

Предусловия: 0 < N < 105.
'''


def checkio(number):
    result = 0
    num_of_pigeons = []
    next_pigeon = [x for x in range(100)]

    while number > 0:
        for x in  next_pigeon:              # Проходим по списку очереди из следующих голубей
            while x > 0:                    # Добавляем группу следующих голубей в общий список
                num_of_pigeons.append(0)
                x -= 1
            for y in range(len(num_of_pigeons)):    # Кормим
                if number > 0:              # Если корм есть, кормим голубей из общего списка
                    num_of_pigeons[y] = num_of_pigeons[y] + 1
                    number -= 1
                else:
                    break
    for z in num_of_pigeons:                # Суммируем покормленных голубей
        if z > 0:
            result += 1
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"