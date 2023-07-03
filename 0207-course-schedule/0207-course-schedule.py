class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        for p in prerequisites:
            premap[p[0]].append(p[1])
        visit = set()
        def dfs(i):
            if i in visit:
                return False
            if premap[i] == []:
                return True
            visit.add(i)
            for e in premap[i]:
                if not dfs(e): return False 
            visit.remove(i)
            premap[i] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True