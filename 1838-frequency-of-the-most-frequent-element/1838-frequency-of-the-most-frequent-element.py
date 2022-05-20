class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        maxf, total = 0, 0
        l = 0
        for r in range(len(nums)):
            total += nums[r]
            if (nums[r]*(r-l+1)) <= total + k:
                maxf = max(maxf, r-l+1)
            else:
                total -= nums[l]
                l += 1                
        return maxf
        '''nums.sort()
        maxf, total = 0, 0
        l, r = 0, 0
        while r < len(nums):
            total += nums[r]
            while (nums[r]*(r-l+1)) > total + k:
                total -= nums[l]
                l += 1
            maxf = max(maxf, r-l+1)
            r += 1
        return maxf'''
        