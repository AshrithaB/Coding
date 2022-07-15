class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("infinity")
        ans = 0
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l<r:
                curSum = nums[i]+nums[l]+nums[r]
                if curSum == target:
                    return curSum
                elif abs(curSum-target) < diff:
                    diff = abs(curSum-target)
                    ans = curSum
                if curSum < target:
                    l += 1
                else:
                    r -= 1
        return ans
        