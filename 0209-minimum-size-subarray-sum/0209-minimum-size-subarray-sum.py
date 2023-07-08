class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = len(nums)+1
        l = 0
        cursum = 0
        for r in range(len(nums)):
            cursum += nums[r]
            while l<=r and cursum >= target:
                minLen = min(minLen, r-l+1)
                cursum -= nums[l]
                l += 1
        return minLen if minLen != len(nums)+1 else 0