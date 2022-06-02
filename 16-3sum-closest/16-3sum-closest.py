class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("infinity")
        res = 0
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l<r:
                curSum = nums[i]+nums[l]+nums[r]
                if curSum == target:
                    return target
                elif abs(curSum-target) < diff:
                    diff = abs(curSum - target)
                    res = curSum
                if curSum > target:
                    r -= 1
                else:
                    l += 1 
        return res