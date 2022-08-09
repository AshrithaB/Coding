class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0 for i in range(amount+1)] for i in range(len(coins)+1)]
        for i in range(amount+1):
            dp[0][i] = math.inf - 1
        for i in range(1, amount+1):
            if i % coins[0] == 0:
                dp[1][i] = i // coins[0]
            else:
                dp[1][i] = math.inf - 1
        for i in range(2, len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    dp[i][j] = min(1+dp[i][j-coins[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(coins)][amount] if dp[len(coins)][amount] != math.inf-1 else -1
        