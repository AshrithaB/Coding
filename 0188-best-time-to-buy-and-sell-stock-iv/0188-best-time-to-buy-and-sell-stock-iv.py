class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices))]
        for t in range(0, k):
            pos = -prices[0]
            profit = 0
            for i in range(len(prices)):
                pos = max(pos, dp[i]-prices[i])
                profit = max(profit, pos+prices[i])
                dp[i] = profit
        return profit