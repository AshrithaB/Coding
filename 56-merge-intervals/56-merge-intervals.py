class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        i = 1
        while i < len(intervals):
            pairA, pairB = res[-1], intervals[i]
            if pairA[1] >= pairB[0]:
                res[-1][1] = max(pairA[1], pairB[1])
            else:
                res.append(pairB)
            i += 1
        return res
        
        