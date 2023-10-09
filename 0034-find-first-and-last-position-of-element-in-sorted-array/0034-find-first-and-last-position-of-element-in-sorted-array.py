class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        h = len(nums)-1
        start, end = -1, -1
        while l <= h:
            m = (l + h)//2
            if nums[m] == target:
                if m-1 > -1 and nums[m] == nums[m-1]:
                    h = m-1
                else:
                    start = m
                    break
            elif nums[m] > target:
                h = m-1
            else:
                l = m+1
        if start == -1:
            return [start, end]
        l = 0
        h = len(nums)-1
        while l <= h:
            m = (l + h)//2
            if nums[m] == target:
                if m+1 < len(nums) and nums[m] == nums[m+1]:
                    l = m+1
                else:
                    end = m
                    break
            elif nums[m] > target:
                h = m-1
            else:
                l = m+1
        return [start, end]