class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        median = []
        start = end = 0
        for end in range(k, len(nums)+1):
            arr = sorted(nums[start:end])
            if k % 2:
                median.append(arr[k//2])
            else:
                median.append((arr[k//2] + arr[(k//2) - 1]) / 2)
            start += 1
        return median