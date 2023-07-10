class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = -k, k
        res = float('inf')
        while l<=r:
            res = min(res, (nums[-1] + l) - (nums[0] + r))
            l += 1
            r -= 1
        return res if res > 0 else 0
    
