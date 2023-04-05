from typing import List


class Solution:
    def __init__(self, prices):
        self.prices = prices
        self.test()

    def maxProfit(self, prices: List[int]) -> int:
        profit = -1
        low = prices[0]
        for price in prices:
            if price < low:
                low = price
            profit = max(profit, price - low)
        return profit

    def test(self):
        print(self.maxProfit(self.prices))


prices = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1],
          [3, 2, 6, 5, 0, 3], [2, 4, 1]]

for price in prices:
    s = Solution(price)
