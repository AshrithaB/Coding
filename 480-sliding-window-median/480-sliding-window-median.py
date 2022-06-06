class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        median = []
        l = 0
        for r in range(k, len(nums)+1):
            arr = sorted(nums[l:r])
            if k%2 == 0:
                median.append((arr[k//2] + arr[(k//2)-1])/2)
            else:
                median.append(arr[k//2])
            l += 1
        return median
        