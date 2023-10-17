class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums)-1
        while s <= e:
            m = (s + e)//2
            if nums[m] == target:
                return m
            elif nums[s] <= nums[m]:
                if target < nums[s] or nums[m] < target:
                    s = m + 1
                else:
                    e = m - 1
            else:
                if nums[e] < target or target < nums[m]:
                    e = m - 1
                else:
                    s = m + 1
        return -1