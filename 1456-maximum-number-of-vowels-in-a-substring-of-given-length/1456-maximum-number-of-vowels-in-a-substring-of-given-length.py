class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        vc = 0
        for i in range(k):
            if s[i] in vowels:
                vc += 1
        maxvc = vc
        l = 0
        for r in range(k,len(s)):
            if s[l] in vowels:
                vc -= 1
            l += 1
            if s[r] in vowels:
                vc += 1
            maxvc = max(maxvc, vc) 
        return maxvc
        