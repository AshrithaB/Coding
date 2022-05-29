class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)<2: 
            return 0
        elif len(nums) == k: 
            return max(nums) - min(nums)
        nums.sort()
        minDiff = max(nums[:k]) - min(nums[:k])
        l = 1
        for r in range(k, len(nums)):            
            curDiff = max(nums[l:r+1]) - min(nums[l:r+1])
            minDiff = min(minDiff, curDiff)
            l += 1
        return minDiff