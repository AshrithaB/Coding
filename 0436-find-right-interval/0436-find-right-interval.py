class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        new_inter = []
        for i, inter in enumerate(intervals):
            new_inter.append([inter,i])
        new_inter.sort()
        res = [-1 for _ in range(len(intervals))]
        for i, inter in enumerate(new_inter):
            end = inter[0][1]
            s, e = i, len(new_inter)-1
            while s <= e:
                m = (s+e)//2
                if new_inter[m][0][0] >= end:
                    e = m - 1
                else:
                    s = m + 1
            if -1 < s < len(new_inter):
                res[new_inter[i][1]] = new_inter[s][1]
        return res