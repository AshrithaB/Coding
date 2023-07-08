class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        for r in range(1, len(prices)):
            while l < r and prices[l] > prices[r]:
                l += 1
            profit += prices[r] - prices[l]
            l = r
        return profit