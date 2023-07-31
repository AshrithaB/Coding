class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k+1):
            temp_prices = prices.copy()
            for s,t,c in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + c < temp_prices[t]:
                    temp_prices[t] = prices[s] + c
            prices = temp_prices
        return prices[dst] if prices[dst] != float("inf") else -1
        
