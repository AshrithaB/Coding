class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def subsetsum(n, arr, s):
            t = [[False]*(s+1) for _ in range(n+1)]
            for i in range(n+1):
                t[i][0] = True
            for i in range(1, n+1):
                for j in range(1, s+1):
                    if arr[i-1] <= j:
                        t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
                    else:
                        t[i][j] = t[i-1][j]
            return t[n][s]
            
        if sum(nums) % 2 != 0:
            return False
        else:
            return subsetsum(len(nums), nums, sum(nums)//2)