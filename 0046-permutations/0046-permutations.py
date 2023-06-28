class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            prems = self.permute(nums)
            for p in prems:
                p.append(n)
                res.append(p)
            nums.append(n)
        
        return res