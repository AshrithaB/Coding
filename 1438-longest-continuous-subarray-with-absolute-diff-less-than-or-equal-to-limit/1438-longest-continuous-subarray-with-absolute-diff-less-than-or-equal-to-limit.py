class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        decQ = collections.deque()
        incQ = collections.deque()
        l = r = 0
        while r < len(nums):
            while decQ and nums[r] > decQ[-1]: 
                decQ.pop()
            decQ.append(nums[r])    
            while incQ and nums[r] < incQ[-1]: 
                incQ.pop()
            incQ.append(nums[r])
            while decQ[0] - incQ[0] > limit:
                if decQ[0] == nums[l]:
                    decQ.popleft()
                if incQ[0] == nums[l]:
                    incQ.popleft()
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res