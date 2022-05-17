class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        seen = 0
        l = 0
        maxLen = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                if seen == 0:
                    seen = 1 
                else:
                    l = ind+1
                    seen = 1
                ind = r
            if seen == 1:
                maxLen = max(maxLen, r-l)
        if maxLen == 0:
            if nums[0] == 0:
                return 0
            else:
                return len(nums)-1
        return maxLen 
                
        