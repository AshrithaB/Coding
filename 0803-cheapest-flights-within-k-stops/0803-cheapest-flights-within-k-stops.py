class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf") for _ in range(n)]
        prices[src] = 0
        temp_prices = [float("inf") for _ in range(n)]
        temp_prices[src] = 0
        for i in range(k+1):
            for s,t,c in flights:
                if prices[s] + c < prices[t]:
                    temp_prices[t] = min(temp_prices[t], prices[s] + c)
            for i, t in enumerate(temp_prices):
                prices[i] = t
        return prices[dst] if prices[dst] != float("inf") else -1
        
