class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        L, res = len(nums), [[]]
        mask = 2**L - 1
        while mask:
            copy = mask
            i = L-1
            subset = []
            while copy:
                if copy & 1:
                    subset.append(nums[i])
                i -= 1
                copy >>= 1
            res.append(subset)
            mask -= 1
        return res