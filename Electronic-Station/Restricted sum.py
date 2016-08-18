def checkio(data):
    index = len(data)-1
    x = 0
    def func(len_data, data):
        if len_data >= 0:
            nonlocal x
            x += data[len_data]
            func(len_data-1, data)
        return x
    print(func(index, data))
    return func(index, data)

checkio([1, 2, 3, 7, 10, 15])