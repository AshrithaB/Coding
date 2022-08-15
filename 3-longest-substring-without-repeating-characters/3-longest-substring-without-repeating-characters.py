class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxLen = 0
        l = 0
        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r], 0)
            while len(seen) != r-l+1:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l += 1
            maxLen = max(maxLen, r-l+1)
        return maxLen