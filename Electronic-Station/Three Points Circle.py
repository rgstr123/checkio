from math import sqrt

def checkio(data):
    (x1, y1), (x2, y2), (x3, y3) = eval(data)

    # Уравнение нашёл тут http://www.cyberforum.ru/geometry/thread1190053.html

    center_x = (((y1-y2)*((x3**2)+(y3**2))) + ((y2-y3)*((x1**2)+(y1**2))) + ((y3-y1)*((x2**2)+(y2**2)))) / (2*((x1-x2)*(y3-y1)-((y1-y2)*(x3-x1))))
    center_y = (((x1-x2)*((x3**2)+(y3**2))) + ((x2-x3)*((x1**2)+(y1**2))) + ((x3-x1)*((x2**2)+(y2**2)))) / (2*((x1-x2)*(y3-y1)-((y1-y2)*(x3-x1))))
    r = sqrt((x1 - abs(center_x)) ** 2 + (y1 - abs(center_y)) ** 2)


    # # Вычисляем растояние между точками
    # ab = math.hypot(int(data[1]) - int(data[0]), int(data[3]) - int(data[2]))
    #             # ab = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)               # Можно и так
    # bc = math.hypot(int(data[3]) - int(data[2]), int(data[5]) - int(data[4]))
    # ac = math.hypot(int(data[1]) - int(data[0]), int(data[5]) - int(data[4]))
    # print("ab",ab)
    # print("bc",bc)
    # print("ac",ac)
    #
    # # Найдём полупериметр треугольника (нужно для нахождения площали)
    # p = (ab+bc+ac) / 2
    # print("p",p)
    #
    # # Найдём площадь треугольника
    # k = math.sqrt(p*(p-ab)*(p-bc)*(p-ac))
    # print("k", k)
    #
    # # Найдём радиус
    # r = (ab * bc * ac) / (4*k)
    # print("r",r)


    return "(x-{:g})^2+(y-{:g})^2={:g}^2".format(round(abs(center_x), 2), round(abs(center_y), 2), round(r, 2))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
