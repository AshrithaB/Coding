class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1, t2, t3, t4 = -prices[0], float('-inf'), float('-inf'), float('-inf')
        for p in prices:
            t1 = max(t1, -p)
            t2 = max(t2, t1+p)
            t3 = max(t3, t2-p)
            t4 = max(t4, t3+p)
        return max(t4, 0)