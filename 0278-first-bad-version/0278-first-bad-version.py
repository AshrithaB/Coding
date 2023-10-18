# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s = 1
        e = n
        while s < e:
            m = (s + e)//2
            ans = isBadVersion(m)
            if ans == False:
                s = m + 1
            else:
                e = m
        return e