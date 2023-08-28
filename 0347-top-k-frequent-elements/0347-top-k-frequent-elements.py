class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        res = []
        for key,val in hashmap.items():
            res.append([val,key])
        res.sort(reverse = True)
        elem = []
        for r in res:
            elem.append(r[1])
            if len(elem) == k:
                return elem
        return elem