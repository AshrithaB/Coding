class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s = 0
        e = len(nums)-1
        while s < e:
            m = (s+e)//2
            if m%2 == 0:
                if nums[m] == nums[m+1]:
                    s = m + 2
                else:
                    e = m
            else:
                if nums[m] == nums[m-1]:
                    s = m + 1
                else:
                    e = m
        return nums[s]