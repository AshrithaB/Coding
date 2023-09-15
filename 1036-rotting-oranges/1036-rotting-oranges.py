class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        t = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for dr, dc in [[-1,0],[0,1],[1,0],[0,-1]]:
                    r,c = dr+i, dc+j
                    if -1 < r < rows and -1 < c < cols and grid[r][c] == 1:
                        q.append((r,c))
                        grid[r][c] = 2
            t += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return t-1 if t else 0