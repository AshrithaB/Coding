class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        minLen = float("infinity")
        q = collections.deque()
        curSum = 0
        l = 0
        for r in range(len(nums)):
            curSum += nums[r]
            if curSum >= k:
                minLen = min(minLen, r+1)
            curr = -1
            while q and curSum - q[0][0] >= k:
                curr = q[0]
                q.popleft()
            if curr != -1:
                minLen = min(minLen, r-curr[1])
            while q and curSum < q[-1][0]:
                q.pop()
            q.append([curSum,r]) 
        return minLen if minLen != float("infinity") else -1