class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        min_num, max_num = math.inf, -math.inf
        while i < len(nums)-1 and nums[i] <= nums[i+1]:
            i += 1
        if i == len(nums)-1:
            return 0
        while j > 0 and nums[j] >= nums[j-1]:
            j -= 1
        for k in range(i, j+1):
            min_num = min(min_num, nums[k])
            max_num = max(max_num, nums[k])
        while i > 0 and nums[i-1] > min_num:
            i -= 1
        while j < len(nums)-1 and nums[j+1] < max_num:
            j += 1
        return j-i+1
        
        