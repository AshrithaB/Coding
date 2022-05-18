class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        out = [-1]*len(nums)
        l = 0
        s = sum(nums[:k+k])
        for r in range(k,len(nums)-k):
            s += nums[r+k] 
            out[r] = s // (r+k-l+1)
            s -= nums[l]
            l += 1
        return out