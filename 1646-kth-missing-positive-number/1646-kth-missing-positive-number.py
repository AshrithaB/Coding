class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = 0
        e = len(arr)
        while s < e:
            m = (s+e)//2
            offset = arr[m] - m - 1
            if offset >= k:
                e = m
            elif offset < k:
                s = m + 1
        return s + k 
