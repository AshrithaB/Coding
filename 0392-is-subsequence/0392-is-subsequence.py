class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        l = 0
        for r in range(len(t)):
            if l < len(s) and t[r] == s[l]:
                l += 1
        return l == len(s)