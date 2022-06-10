class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 1000000007
        res = 0
        hashMap = {}
        for ch in arr:
            hashMap[ch] = 1 + hashMap.get(ch, 0)
        for i in hashMap:
            for j in hashMap:
                k = target - i - j
                if k not in hashMap:
                    continue
                if i==j and j==k:
                    res += (hashMap[i] * (hashMap[i]-1) * (hashMap[i]-2)) // 6
                elif i==j and j!=k:
                    res += ((hashMap[i] * (hashMap[i]-1)) // 2) * hashMap[k]
                elif i<j and j<k:
                    res += hashMap[i] * hashMap[j] * hashMap[k] 
        return res%mod
        