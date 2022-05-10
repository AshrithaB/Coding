class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, maxLen, unique = 0, 0, set()
        for end in range(len(s)):
            while s[end] in unique:
                unique.remove(s[start])
                start += 1
            unique.add(s[end])
            maxLen = max(maxLen, end - start +1)
        return maxLen