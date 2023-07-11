class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cursum = 0
        minlen = float('inf')
        l = 0
        for r in range(len(nums)):
            cursum += nums[r]
            while l <= r and cursum >= target:
                minlen = min(minlen, r-l+1)
                cursum -= nums[l]
                l += 1
        return minlen if minlen != float('inf') else 0