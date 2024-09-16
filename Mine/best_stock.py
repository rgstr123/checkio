'''
Вам даны текущие цены на акции. Вам необходимо выяснить за какие акции дают большую цену.
Input: Словарь (dict), в котором ключи - это рыночный код, а значение - это цена за акцию(float)
Output: Строка, рыночный код
'''


def best_stock(data: dict[str, float]) -> str:
    max_stock_ticker = ""
    max_stock_value = 0
    for ticker, value in data.items():
        if value > max_stock_value:
            max_stock_value = value
            max_stock_ticker = ticker
    print(max_stock_ticker)
    return max_stock_ticker


assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"

print("The mission is done! Click 'Check Solution' to earn rewards!")