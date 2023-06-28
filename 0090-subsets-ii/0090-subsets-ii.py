class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, subset):
            if i >= len(nums):
                if subset not in res:
                    res.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            while i < len(nums)-1 and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1, subset)
        dfs(0, [])
        return res