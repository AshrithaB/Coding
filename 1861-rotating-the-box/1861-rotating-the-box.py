class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        for i in range(m):
            for j in range(n-1, -1, -1):
                if box[i][j] == '#':
                    empty = j + 1
                    while empty < n and box[i][empty] == '.':
                        empty += 1
                    if empty < n and box[i][empty] == '.':
                        box[i][empty] = '#'
                        box[i][j] = '.'
                    elif empty-1 < n and box[i][empty-1] == '.':
                        box[i][empty-1] = '#'
                        box[i][j] = '.'
        res = [['' for i in range(m)] for j in range(n)]
        k = m-1
        for i in range(m):
            for j in range(n):
                res[j][k] = box[i][j]
            k -= 1
        return res