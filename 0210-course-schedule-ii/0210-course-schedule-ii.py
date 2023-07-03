class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        premap = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            premap[c].append(p)
        visit = set()
        def dfs(i):
            if i in visit:
                return False
            if premap[i] == []:
                if i not in res:
                    res.append(i)
                return True
            visit.add(i)
            for e in premap[i]:
                if not dfs(e):
                    return False
            visit.remove(i)
            premap[i] = []
            res.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res