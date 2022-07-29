class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        minLen = float('infinity')
        curSum = 0
        q = collections.deque()
        l = 0
        for r in range(len(nums)):
            curSum += nums[r]
            if curSum >= k:
                minLen = min(minLen, r+1)
            cur = -1
            while q and curSum - q[0][0] >= k:
                cur = q[0]
                q.popleft()
            if cur != -1:
                minLen = min(minLen, r-cur[1])
            while q and curSum < q[-1][0]:
                q.pop()
            q.append([curSum, r])
        return minLen if minLen != float('infinity') else -1