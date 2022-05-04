import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len, start, min_sum = math.inf, 0, 0 
        for end in range(len(nums)):
            min_sum += nums[end]
            while min_sum >= target:
                min_len = min(min_len, end-start+1)
                min_sum -= nums[start]
                start += 1
        if min_len == math.inf:
            return 0
        return min_len
        