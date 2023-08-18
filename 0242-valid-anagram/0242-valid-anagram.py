class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashsets = {}
        hashsett = {}
        for i in range(len(s)):
            if s[i] not in hashsets:
                hashsets[s[i]] = 0
            hashsets[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in hashsett:
                hashsett[t[i]] = 0
            hashsett[t[i]] += 1
        if hashsets == hashsett:
            return True
        return False