class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        po, ao = set(), set()
        def dfs(i, j, visit):
            visit.add((i,j))
            dr = [[1,0],[0,1],[-1,0],[0,-1]]
            for r, c in dr:
                ri, cj = i+r, j+c
                if (-1 < ri < rows and -1 < cj < cols and 
                    heights[ri][cj] >= heights[i][j] and (ri,cj) not in visit):
                    dfs(ri, cj, visit)
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0: 
                    dfs(r,c,po)
                if r == rows - 1 or c == cols-1:
                    dfs(r,c,ao)
        return po & ao