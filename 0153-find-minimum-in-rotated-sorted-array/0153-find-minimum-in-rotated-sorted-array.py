class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums)-1
        res = float("inf")
        while s <= e:
            if nums[s] < nums[e]:
                res = min(res, nums[s])
                break
            m = (s+e)//2
            res = min(res, nums[m])
            if nums[s] <= nums[m]:
                s = m + 1
            elif nums[m] < nums[e]:
                e = m - 1
        return res