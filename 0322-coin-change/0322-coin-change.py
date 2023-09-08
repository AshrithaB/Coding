
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        t = [[-1]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            t[i][0] = 0
        for i in range(amount+1):
            t[0][i] = sys.maxsize - 1
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    t[i][j] = min(1 + t[i][j-coins[i-1]], t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        return t[len(coins)][amount] if t[len(coins)][amount] != sys.maxsize - 1 else -1