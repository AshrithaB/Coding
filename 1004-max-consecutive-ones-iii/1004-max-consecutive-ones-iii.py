class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        for j in range(len(nums)):
            k -= 1-nums[j]
            if k < 0:
                k += 1-nums[i]
                i += 1
        return j-i+1
                
        '''seen, maxlen = 0, 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                seen += 1
                while seen > k:
                    if nums[l] == 0:
                        seen -= 1
                    l += 1
            maxlen = max(maxlen, r-l+1)
        return maxlen'''