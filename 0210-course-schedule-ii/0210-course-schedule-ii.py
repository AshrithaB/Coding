class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        premap = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            premap[c].append(p)
        visit, cycle = set(), set()
        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True
            cycle.add(i)
            for e in premap[i]:
                if not dfs(e):
                    return False
            cycle.remove(i)
            visit.add(i)
            res.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res