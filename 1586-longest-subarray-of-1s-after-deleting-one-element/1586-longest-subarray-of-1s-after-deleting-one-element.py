class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxones = 0
        l = 0
        c = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                c += 1
            while l<=r and c >1:
                maxones = max(maxones, r-l-1)
                if nums[l] == 0:
                    c -= 1
                l += 1
        maxones = max(maxones, r-l)
        return maxones