class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        for g in grid:
            print(g)
            l, h = 0, len(g)-1
            while l<=h:
                m =(l+h)//2
                if g[m] < 0:
                    h = m-1
                else:
                    l = m+1
            neg += len(g)-l
        return neg