class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0]*len(nums)
        i = 0
        for n in nums:
            if n:
                res[i] = n
                i += 1
        nums[:] = res[:]
        return         