class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums.copy()]
        for i in range(len(nums)):
            n = nums.pop(0)
            premutes = self.permute(nums)
            for p in premutes:
                p.append(n)
                res.append(p)
            nums.append(n)
        return res
