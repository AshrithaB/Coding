class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        i = len(grid)-1
        j = 0
        while i > -1 and j < len(grid[0]):
            if grid[i][j] < 0:
                count += len(grid[0]) - j
                i -= 1
            else:
                j += 1
        return count
