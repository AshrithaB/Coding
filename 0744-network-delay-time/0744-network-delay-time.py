class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = 0
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append([w,v])
        visit = set()
        minHeap = [[0,k]]
        while minHeap:
            w, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            visit.add(i)
            time = max(time, w)
            for c, j in adj[i]:
                if j not in visit:
                    heapq.heappush(minHeap, [c+w,j])
        return time if len(visit) == n else -1
