class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, maxLen, found = 0, 0, {}
        for end in range(len(s)):
            if s[end] not in found:
                found[s[end]] = 1
            else:
                found[s[end]] += 1
            while sum(found.values()) - max(found.values()) > k:
                found[s[start]] -= 1
                if found[s[start]] == 0:
                    found.pop(s[start])
                start += 1
            maxLen = max(maxLen, end-start+1)
        return maxLen
            