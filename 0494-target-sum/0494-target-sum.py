class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == abs(target):
                return 1
            else:
                return 0
        if (sum(nums)+target) % 2 == 1:
            return 0
        s1 = (sum(nums)+target)//2
        if s1 < 0:
            return 0

        def countsubsetsum(n, arr, s):
            t = [[0]*(s+1) for _ in range(n+1)]
            for i in range(0,n+1):
                t[i][0] = 1
            print(t)
            for i in range(1, n+1):
                for j in range(1, s+1):
                    if arr[i - 1] == 0:
                        t[i][j] = t[i-1][j];
                    elif arr[i-1] <= j:
                        t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
                    else:
                        t[i][j] = t[i-1][j]
            return pow(2, arr.count(0)) * t[n][s]
        
        return countsubsetsum(len(nums), nums, s1)