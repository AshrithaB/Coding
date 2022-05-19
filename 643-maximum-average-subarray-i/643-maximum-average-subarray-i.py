class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k-1])
        maxavg = -float("infinity")
        l = 0
        for r in range(k-1,len(nums)):
            s += nums[r]
            maxavg = max(maxavg, s/k)
            s -= nums[l]
            l += 1
        return maxavg
        