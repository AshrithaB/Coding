import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, maxSum, minLen = 0, 0, float("inf")
        for end in range(len(nums)):
            maxSum += nums[end]
            while maxSum >= target:
                minLen = min(minLen, end-start+1)
                maxSum -= nums[start]
                start += 1
        return 0 if minLen == float("inf") else minLen