class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        minHeap = [[grid[0][0],0,0]]
        while minHeap:
            t,r,c = heapq.heappop(minHeap)
            if r == rows-1 and c == cols-1:
                return t
            if (r,c) in visit:
                continue
            visit.add((r,c))
            for dr, dc in [[0,1], [1,0], [-1,0], [0,-1]]:
                row, col = dr+r, dc+c
                if (row in range(rows) and col in range(cols) and 
                    (row, col) not in visit):
                    heapq.heappush(minHeap, [max(t, grid[row][col]), row, col])