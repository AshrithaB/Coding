class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            
            l, r = i+1, len(nums)-1
            while l<r:
                curSum = nums[i]+nums[l]+nums[r]
                if curSum < 0:
                    l += 1
                elif curSum > 0:
                    r -= 1
                else:
                    triplet = [nums[i],nums[l],nums[r]]
                    if triplet not in res:
                        res.append(triplet)
                    l += 1
        return res