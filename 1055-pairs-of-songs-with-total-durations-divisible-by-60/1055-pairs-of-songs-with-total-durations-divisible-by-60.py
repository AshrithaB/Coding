class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        diffhash = {}
        res = 0
        for i in range(len(time)):
            time[i] = time[i] % 60
            diffhash[time[i]] = 1 + diffhash.get(time[i], 0)
        for t in diffhash:
            if t == 0 or t == 30:
                n = diffhash[t]
                if n > 1:
                    res += ((n-1) * n) // 2
            elif t < 30:
                if 60-t in diffhash:
                    res += diffhash[t] * diffhash[60-t]
        return res
