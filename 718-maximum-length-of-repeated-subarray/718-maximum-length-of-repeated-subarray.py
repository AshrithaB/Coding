class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for j in range(len(nums2)+1)] for i in range(len(nums1)+1)]
        ans = 0
        for i in range(len(nums1)-1, -1, -1):
            for j in range(len(nums2)-1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                ans = max(ans, dp[i][j])
        return ans
            