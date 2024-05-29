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

Solution().maxProfit([7,1,5,3,6,4])