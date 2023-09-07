class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1count = {}
        s2count = {}
        for s in range(len(s1)):
            s1count[s1[s]] = 1 + s1count.get(s1[s], 0)
            s2count[s2[s]] = 1 + s2count.get(s2[s], 0)
        if s1count == s2count:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            s2count[s2[l]] -= 1
            if s2count[s2[l]] == 0:
                del s2count[s2[l]]
            l += 1
            s2count[s2[r]] = 1 + s2count.get(s2[r], 0)
            if s1count == s2count:
                return True
        return False