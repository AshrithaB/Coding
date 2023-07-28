class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src:[] for src, _ in tickets}
        tickets.sort()
        for f, t in tickets:
            adj[f].append(t)
        itinerary = ["JFK"]

        def dfs(ticket):
            if len(itinerary) == len(tickets)+1:
                return True
            if ticket not in adj:
                return False
            temp = list(adj[ticket])
            for i, v in enumerate(temp):
                adj[ticket].pop(i)
                itinerary.append(v)
                if dfs(v):
                    return True
                adj[ticket].insert(i, v)
                itinerary.pop()
            return False
  
        dfs("JFK")
        return itinerary