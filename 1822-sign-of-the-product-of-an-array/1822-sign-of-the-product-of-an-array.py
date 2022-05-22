class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: 
            return 0
        c = 1
        for n in nums:
            if n < 0:
                c *= -1
        return c
        