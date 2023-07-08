class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices))]
        for t in range(0, 2):
            profit = 0
            l = -prices[0]
            for r in range(1, len(prices)):
                l = max(l, dp[r]-prices[r])
                profit = max(profit, l + prices[r])
                dp[r] = profit
        return profit