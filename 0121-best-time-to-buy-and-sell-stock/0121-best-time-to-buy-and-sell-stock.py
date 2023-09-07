class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for r in range(len(prices)):
            if buy < prices[r]:
                profit = max(profit, prices[r]-buy)
            else:
                buy = prices[r]
        return profit