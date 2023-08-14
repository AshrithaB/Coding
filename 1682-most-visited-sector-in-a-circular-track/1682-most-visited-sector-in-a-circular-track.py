class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        temp = [0]*n
        maxcount = 0
        l = rounds[0]
        temp[l-1] += 1
        l += 1
        for r in rounds[1:]:
            while l%n != (r+1)%n:
                temp[(l%n)-1] += 1
                maxcount = max(maxcount, temp[(l%n)-1])
                l += 1
        res = []
        for i, t in enumerate(temp):
            if t == maxcount:
                res.append(i+1)
        return res
        
        