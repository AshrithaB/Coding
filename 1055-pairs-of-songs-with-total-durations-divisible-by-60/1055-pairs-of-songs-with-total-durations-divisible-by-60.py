class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashmap = {}
        for i in range(len(time)):
            time[i] %= 60
            hashmap[time[i]] = 1 + hashmap.get(time[i], 0)
        res = 0
        for k in hashmap:
            if k == 0 or k == 30:
                if hashmap[k] > 1:
                    res += (hashmap[k] * (hashmap[k] - 1))//2
            elif k < 30:
                if 60-k in hashmap:
                    res += hashmap[k] * hashmap[60-k]
        return res
            