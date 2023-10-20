class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s = 0
        e = len(arr)-1
        while s < e:
            m = (s+e)//2
            if arr[m-1] < arr[m] > arr[m+1]:
                return m
            elif arr[m-1] < arr[m]:
                s = m + 1
            else:
                e = m