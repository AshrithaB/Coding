class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if len(nums) == 1:
            return nums
        lastPeakInd = -1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                lastPeakInd = i
        if lastPeakInd == -1:
            for k in range(len(nums)//2):
                nums[k], nums[len(nums)-k-1] = nums[len(nums)-k-1], nums[k]
            return
        peakNum = nums[lastPeakInd]
        index = lastPeakInd
        for i in range(lastPeakInd+1, len(nums)):
            if nums[i]>nums[lastPeakInd-1] and nums[i]<nums[index]:
                index = i
        nums[lastPeakInd-1], nums[index] = nums[index], nums[lastPeakInd-1]
        nums[lastPeakInd:] = sorted(nums[lastPeakInd:])   
        return
            
        