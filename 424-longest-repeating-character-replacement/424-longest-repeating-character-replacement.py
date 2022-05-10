class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, maxLen, found = 0, 0, {}
        maxf = 0
        for end in range(len(s)):
            found[s[end]] = 1 + found.get(s[end], 0)
            maxf = max(maxf, found[s[end]])
            while (end-start+1) - maxf > k:
                found[s[start]] -= 1
                start += 1
            maxLen = max(maxLen, end-start+1)
        return maxLen
    