class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = [0] * len(prices)
        right = [0] * len(prices)
        lmin, rmax = prices[0], prices[-1]
        for i in range(1, len(prices)):
            if lmin > prices[i]:
                lmin = prices[i]
            left[i] = max(left[i-1], prices[i] - lmin)
        profit = left[-1]
        for i in range(len(prices)-2, -1, -1):
            if rmax < prices[i]:
                rmax = prices[i]
            right[i] = max(right[i+1], rmax - prices[i])
            profit = max(profit, right[i+1]+left[i])
        return profit