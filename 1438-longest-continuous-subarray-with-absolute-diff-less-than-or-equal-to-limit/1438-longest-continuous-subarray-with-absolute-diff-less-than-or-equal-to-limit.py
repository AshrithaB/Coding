class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = l = 0
        incQ = collections.deque()
        decQ = collections.deque()
        for r in range(len(nums)):
            while decQ and decQ[-1] < nums[r]:
                decQ.pop()
            decQ.append(nums[r])
            while incQ and incQ[-1] > nums[r]:
                incQ.pop()
            incQ.append(nums[r])
            while decQ[0] - incQ[0] > limit:
                if nums[l] == decQ[0]:
                    decQ.popleft()
                if nums[l] == incQ[0]:
                    incQ.popleft()
                l += 1
            ans = max(ans, r-l+1)
        return ans