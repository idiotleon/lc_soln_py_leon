"""
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    Time Complexity:    O(`LEN`)
    Space Complexity:   O(1)

    Reference:
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/editorial/

    @author: Leon
"""


from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # not used
        # LEN = len(prices)
        RANGE = 1e4
        min_price = RANGE + 7
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
