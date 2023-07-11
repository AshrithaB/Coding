class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pos = -prices[0]
        profit = 0
        for p in prices:
            pos = max(pos, -p)
            profit = max(profit, pos+p)
        return profit