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
        '''subarr, curavg = 0, 0
        for i in range(k-1):
            curavg += arr[i]
        for r in range(k-1, len(arr)):
            curavg += arr[r]
            if curavg/k >= threshold:
                subarr += 1
            curavg -= arr[r-k+1]
        return subarr'''