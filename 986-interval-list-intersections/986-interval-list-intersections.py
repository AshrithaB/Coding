class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        a = b = 0
        while a < len(firstList) and b < len(secondList):
            s1, e1 = firstList[a][0], firstList[a][1]
            s2, e2 = secondList[b][0], secondList[b][1]
            if s1 <= e2 and s2 <= e1:
                res.append([s1 if s1>s2 else s2, e1 if e1<e2 else e2])
            if e1 < e2:
                a += 1
            else:
                b += 1
        return res