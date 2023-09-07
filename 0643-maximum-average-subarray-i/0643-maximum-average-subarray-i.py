class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxavg = float('-inf')
        total = 0
        l = 0
        for r in range(len(nums)):
            total += nums[r]
            if r >= k-1:
                maxavg = max(maxavg, total/k)
                total -= nums[l]
                l += 1
        return maxavg