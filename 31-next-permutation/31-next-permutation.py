class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        lastind = -1
        i = 1
        while i<len(nums):
            if nums[i] > nums[i-1]:
                lastind = i
            i += 1
        if lastind == -1:
            for k in range(len(nums)//2):
                nums[k], nums[len(nums)-k-1] = nums[len(nums)-k-1], nums[k]
            return
        index = lastind
        for j in range(lastind+1, len(nums)):
            if nums[j]>nums[lastind-1] and nums[j]<nums[index]:
                index = j
        nums[index], nums[lastind-1] = nums[lastind-1], nums[index]
        nums[lastind:] = sorted(nums[lastind:])
        return
        