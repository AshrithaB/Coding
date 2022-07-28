class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        c = 0
        prev, curr = 0, 1
        i = 1
        while i < len(s):
            if s[i-1] != s[i]:
                c += min(prev, curr)
                prev = curr
                curr = 1
            else:
                curr += 1
            i += 1
        c += min(prev, curr)
        return c