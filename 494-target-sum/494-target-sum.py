class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n, s = len(nums), 0
        for i in range(n):
            s += nums[i]
        if s < target or (s+target) % 2 != 0:
            return 0        
        dp = [[0 for i in range(s+1)] for i in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(s+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        s1 = (s+target)//2
        return dp[n][s1]


