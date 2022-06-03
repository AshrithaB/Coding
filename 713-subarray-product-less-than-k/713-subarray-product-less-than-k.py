class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: return 0
        prod, res = 1, 0
        l, r = 0, 0
        while r<len(nums):
            prod *= nums[r]
            while prod >= k:
                prod //= nums[l]
                l += 1
            res += r-l+1
            r += 1
        return res
                
        