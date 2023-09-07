class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxvowel = 0
        l = 0
        countvowel = 0
        for r in range(len(s)):
            if s[r] in 'aeiou':
                countvowel += 1
            if countvowel == k:
                return k
            if r >= k-1:
                maxvowel = max(maxvowel, countvowel)
                if s[l] in 'aeiou':
                    countvowel -= 1
                l += 1
        return maxvowel