class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subarr, curavg = 0, 0
        for i in range(k-1):
            curavg += arr[i]
        for r in range(k-1, len(arr)):
            curavg += arr[r]
            if curavg/k >= threshold:
                subarr += 1
            curavg -= arr[r-k+1]
        return subarr