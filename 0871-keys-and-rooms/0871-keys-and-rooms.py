class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        def dfs(n):
            visit.add(n)
            for nei in rooms[n]:
                if nei not in visit:
                    dfs(nei)

        dfs(0)
        return len(visit) == len(rooms)
        