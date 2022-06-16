class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        hashMap = {}
        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)
        for h in hashMap:
            if k == 0:
                count += hashMap[h] > 1
            elif h+k in hashMap:
                count += 1
        return count