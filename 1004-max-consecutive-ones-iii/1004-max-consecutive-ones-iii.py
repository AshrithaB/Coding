class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        seen, maxlen = 0, 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                seen += 1
                while seen > k:
                    if nums[l] == 0:
                        seen -= 1
                    l += 1
            maxlen = max(maxlen, r-l+1)
        return maxlen