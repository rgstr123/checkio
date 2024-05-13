'''
Мерзкими числами зовутся числа, состоящие только из простых делителей 2, 3 или 5. Последовательность 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ... показывает первые 11 мерзких чисел (1 тоже считается мерзким числом). Напишите программу, которая находит мерзкое число с номером n

ugly_numbers
1, 2, 3, 4, 5, 6, 7, 8, 9,  10, 11 ...
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15 ...

Входные данные: N, int.

Выходные данные: Мерзкое число с номером N, int.

Примеры:

ugly_number(4) == 4
ugly_number(6) == 6
ugly_number(11) == 15
1
2
3
Где используется подобное: Для демонстрации того, что простое решение может быть весьма медленным

Ограничения: Входное число меньше или равно 1500

Миссия позаимствована с соревнований ICPC
'''


'''
Divisibility rules 

A number is divisible by 2 if and only if its last digit is even, i.e., is equal to 2,4,6, or 8.
A number is divisible by 3 if and only if the sum of its digits is divisible by 3.
A number is divisible by 4 if and only if its last two digits form a number divisible by 4.
A number is divisible by 5 if and only if its last digit is 0 or 5.
A number is divisible by 6 if and only if it is divisible by 2 and by 3.
A number is divisible by 7 if and only if subtracting two times the last digit from the rest gives a number divisible by 7.  EXAMPLE 165 is not divisible by 7 because: the last digit of 165 is 5. The remaining digits give 16. We have 16 - 2*5 = 6, which is not divisible by 7.
	Alternative rule: A number is divisible by 7 if and only if subtracting nine times the last digit from the rest gives a number divisible by 7.
	Alternative rule: A number is divisible by 7 if and only if the alternating sum of blocks of three digits from right to left is divisible by 7.
A number is divisible by 8 if and only if its last three digits form a number divisible by 8.
	Alternative rule: If the hundreds digit is odd, a number is divisible by 8 if and only if the number formed by the last two digits plus 4 is divisible by 8.
A number is divisible by 9 if and only if the sum of its digits is divisible by 9.
A number is divisible by 10 if and only if its last digit is 0.
A number is divisible by 11 if and only if the alternating sum of its digits is divisible by 11.
	Alternative rule: A number is divisible by 11 if and only if adding its digits in blocks of two from right to left we get a number divisible by 11. EXAMPLE 65 is divisible by 11 because: the alternating sum of its digits is 1-6+5=0, which is divisible by 11.
A number is divisible by 12 if and only if it is divisible by 3 and by 4.
A number is divisible by 13 if and only if the alternating sum of blocks of three digits from right to left is divisible by 13.
'''

def ugly_number(n):
    # Инициализация массива для хранения мерзких чисел
    ugly_numbers = [1] * n
    # Индексы для множителей 2, 3, 5
    i2 = i3 = i5 = 0
    
    # Следующее по величине мерзкое число для каждого из множителей
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    
    # Цикл для нахождения n мерзких чисел
    for i in range(1, n):
        # Выбор минимального числа из возможных множителей
        next_ugly_num = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        ugly_numbers[i] = next_ugly_num
        
        # Обновление индекса для множителя, который был использован
        if next_ugly_num == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly_numbers[i2] * 2
        if next_ugly_num == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly_numbers[i3] * 3
        if next_ugly_num == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly_numbers[i5] * 5
    
    # Возврат n-го мерзкого числа
    return ugly_numbers[-1]


assert ugly_number(1) == 1
assert ugly_number(4) == 4
assert ugly_number(6) == 6
assert ugly_number(11) == 15
assert ugly_number(25) == 33
assert ugly_number(23) == 30
assert ugly_number(29) == 75
