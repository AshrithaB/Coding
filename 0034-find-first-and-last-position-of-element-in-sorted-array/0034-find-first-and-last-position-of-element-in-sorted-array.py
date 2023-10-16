class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        l, h = 0, len(nums)-1
        while l <= h:
            m = (l+h)//2
            if nums[m] < target:
                l = m + 1
            else:
                h = m - 1
        if -1 < l < len(nums) and nums[l] == target:
            s = l
            while l < len(nums)-1 and nums[l] == nums[l+1]:
                l = l + 1
            res = [s,l]
            return res
        return res