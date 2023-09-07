class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxones = 0
        l = 0
        c = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                c += 1
            while l <= r and c > k:
                maxones = max(maxones, r-l)
                if nums[l] == 0:
                    c -= 1
                l += 1
        maxones = max(maxones, r-l+1)
        return maxones 