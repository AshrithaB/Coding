class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)<2: 
            return 0
        nums.sort()
        minDiff = nums[k-1] - nums[0]
        for r in range(k, len(nums)):
            minDiff = min(minDiff, nums[r] - nums[r-k+1])
        return minDiff