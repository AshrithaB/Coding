class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 1000000007
        hashMap = {}
        count = 0
        for ch in arr:
            hashMap[ch] = 1 + hashMap.get(ch, 0)
        for i in hashMap:
            for j in hashMap:
                k = target - i - j
                if k not in hashMap: continue
                if i == j and j == k:
                    count += (hashMap[i] * (hashMap[j]-1) * (hashMap[k]-2))//6
                elif i == j and j != k:
                    count += ((hashMap[i] * (hashMap[j]-1))//2) * hashMap[k]
                elif i < j and j < k:
                    count += hashMap[i] * hashMap[j] * hashMap[k]
        return count%mod