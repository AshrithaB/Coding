class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        island = 0
        rows, cols = len(grid), len(grid[0])
        visits = set()
        
        def bfs(r, c):
            q = collections.deque()
            visits.add((r, c))
            q.append((r, c))
            while q:
                r, c = q.popleft()
                directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and col in range(cols) and 
                        grid[row][col] == "1" and (row, col) not in visits):
                        visits.add((row, col))
                        q.append((row, col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visits:
                    bfs(r, c)
                    island += 1                    
        return island