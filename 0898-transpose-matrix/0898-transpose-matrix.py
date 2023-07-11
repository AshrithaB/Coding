class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        new_matrix = [[0] * row for _ in range(col)]
        for r in range(row):
            for c in range(col):
                new_matrix[c][r] = matrix[r][c]
        return new_matrix