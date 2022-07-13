import sys


def maxProfit(prices: list) -> int:
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(price - min_price, profit)
        # print(min_price, profit)

    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
