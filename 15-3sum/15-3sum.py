class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                curSum = nums[i]+nums[l]+nums[r]
                if curSum < 0:
                    l += 1
                elif curSum > 0:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        return res