class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if ops == []:
            return m*n
        res = [m, n]
        for r,c in ops:
            res[0] = min(res[0], r)
            res[1] = min(res[1], c)
        return res[0] * res[1]
        