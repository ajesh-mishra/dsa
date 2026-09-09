"""
Time complexity: O(n)
Space complexity: O(1)
"""


def max_profit(prices: list[int]) -> int:
    profit: int = 0
    new_minimum: int = prices[0]

    for num in prices[1:]:
        if new_minimum > num:
            new_minimum = num
        else:
            profit = max(num - new_minimum, profit)

    return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    assert max_profit(prices) == 5
