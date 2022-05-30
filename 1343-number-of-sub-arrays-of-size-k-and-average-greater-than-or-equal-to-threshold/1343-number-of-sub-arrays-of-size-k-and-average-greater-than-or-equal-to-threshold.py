class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subarr = 0
        curavg = sum(arr[:k])
        if curavg/k >= threshold:
            subarr += 1
        l = 0
        for r in range(k, len(arr)):
            curavg += arr[r] - arr[l]
            l += 1
            if curavg/k >= threshold:
                subarr += 1
        return subarr