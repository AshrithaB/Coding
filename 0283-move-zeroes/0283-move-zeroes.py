class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        c = nums.count(0)
        i, j = 0, 0
        for i in range(len(nums)):
            while j < len(nums)-c and nums[j] != 0:
                j += 1
            if nums[i] != 0 and i > j:
                nums[i], nums[j] = nums[j], nums[i]
