import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in prices[1:]:
            if buy > i:
                buy = i
            profit = max(profit, i - buy)

        print(profit)
        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        buy = sys.maxsize
        profit = 0

        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit

Solution().maxProfit([7,1,5,3,6,4])