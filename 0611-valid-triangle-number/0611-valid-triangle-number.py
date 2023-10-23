class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            s, e = 0, i-1
            while s < e:
                if nums[s]+nums[e] > nums[i]:
                    count += e-s
                    e -= 1
                else:
                    s += 1
        return count
