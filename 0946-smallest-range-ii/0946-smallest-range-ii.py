class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]
        for i in range(len(nums)-1):
            j = i+1
            high = max(nums[-1]-k, nums[i]+k)
            low = min(nums[0]+k, nums[j]-k)
            res = min(res, high-low)
        return res
