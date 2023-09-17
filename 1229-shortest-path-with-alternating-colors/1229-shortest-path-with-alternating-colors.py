class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        for a,b in redEdges:
           adj[a].append([b,1])
        for u,v in blueEdges:
            adj[u].append([v,2])
        ans = [-1 for i in range(n)]
        print(adj)
        q = deque()
        q.append([0,0])
        level = 0
        visit = set()
        while q:
            for i in range(len(q)):
                ind, prevcol = q.popleft()
                if ans[ind] == -1:
                    ans[ind] = level
                for s, (t, edgecol) in enumerate(adj[ind]):
                    if t == -1 or edgecol == prevcol:
                        continue
                    q.append([t, edgecol])
                    adj[ind][s] = [-1, edgecol] 
            level += 1
        return ans
            

