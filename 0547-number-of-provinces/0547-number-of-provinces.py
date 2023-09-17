class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        pro = 0
        adj = {i:[] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]==1:
                    adj[i].append(j)
        visit = set()
        res = []
        def dfs(k):
            visit.add(k)
            for nei in adj[k]:
                if nei not in visit:
                    dfs(nei)

        for i in range(n):
            if i not in visit:
                print(i)
                dfs(i)
                pro += 1
        return pro
                    
