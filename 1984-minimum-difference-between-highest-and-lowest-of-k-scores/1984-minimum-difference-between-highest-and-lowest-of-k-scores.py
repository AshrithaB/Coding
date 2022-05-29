class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)<2: 
            return 0
        elif len(nums) == k: 
            return max(nums) - min(nums)
        nums.sort()
        minDiff = nums[-1]
        l = 0
        for r in range(k-1, len(nums)):
            minDiff = min(minDiff, nums[r] - nums[l])
            l += 1
        return minDiff