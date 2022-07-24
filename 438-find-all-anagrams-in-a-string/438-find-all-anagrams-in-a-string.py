class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        countP, countS = {}, {}
        res = []
        for i in range(len(p)):
            countP[p[i]] = 1 + countP.get(p[i], 0)
            countS[s[i]] = 1 + countS.get(s[i], 0)
        if countP == countS:
            res.append(0)
        l = 0
        for r in range(len(p), len(s)):
            countS[s[l]] -= 1
            if countS[s[l]] == 0:
                del countS[s[l]]
            l += 1
            countS[s[r]] = 1 + countS.get(s[r], 0)
            if countP == countS:
                res.append(l)
        return res        