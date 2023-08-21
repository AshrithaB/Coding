class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(num):
            rob1, rob2 = 0, 0
            for n in num:
                temp = max(n+rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        if len(nums) < 2:
            return max(nums)
        return max(rob1(nums[:-1]), rob1(nums[1:]))