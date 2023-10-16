class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        e = len(nums)-1
        while l <= e:
            m = (l+e)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                e = m-1
        return -1