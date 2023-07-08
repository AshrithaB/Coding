class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        for r in range(1, len(prices)):
            if l < r and prices[l] < prices[r]: 
                profit = max(profit, prices[r]-prices[l])
            while prices[l] > prices[r]:
                l += 1
        return profit