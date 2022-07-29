import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen, curSum = float('infinity'), 0
        l = 0
        for r in range(len(nums)):
            curSum += nums[r]
            while l<=r and curSum >= target:
                minLen = min(minLen, r-l+1)
                curSum -= nums[l]
                l += 1
        return minLen if minLen != float('infinity') else 0