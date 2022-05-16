class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        l = 0
        for r in range(k, len(nums)+1):
            if k%2 == 0: 
                res.append((sorted(nums[l:r])[(k//2)-1] + sorted(nums[l:r])[k//2])/2)
            else:
                res.append(sorted(nums[l:r])[k//2])
            l += 1
        return res
        