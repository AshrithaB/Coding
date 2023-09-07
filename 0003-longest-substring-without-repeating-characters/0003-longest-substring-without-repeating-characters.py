class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        l = 0
        visit = set()
        for r in range(len(s)):
            while s[r] in visit:
                visit.remove(s[l])
                l += 1
            visit.add(s[r])
            maxlen = max(maxlen, r-l+1)
        return maxlen