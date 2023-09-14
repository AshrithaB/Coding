class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        def dfs(i,j):
            board[i][j] = "Z"
            for dr, dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                r,c = dr+i, dc+j
                if -1 < r < rows and -1 < c < cols and board[r][c] == "O":
                    dfs(r,c)
            
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0 or i == rows-1 or j == cols-1:
                    if board[i][j] == "O":
                        dfs(i,j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "Z":
                    board[i][j] = "O"
        