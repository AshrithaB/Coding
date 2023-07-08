class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums.copy()]
        for i in range(len(nums)):
            temp = nums.pop(0)
            prems = self.permute(nums)
            for p in prems:
                p.append(temp)
                res.append(p)
            nums.append(temp)
        return res
        