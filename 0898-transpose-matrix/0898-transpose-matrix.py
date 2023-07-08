class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        res = [[0] * row for c in range(col)]
        for r in range(row):
            for c in range(col):
                if r == c:
                    res[r][c] = matrix[r][c]
                else:
                    res[c][r] = matrix[r][c]                   
        return res