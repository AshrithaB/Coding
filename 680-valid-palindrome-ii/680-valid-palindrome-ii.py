class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrom(w, l, r):
            while l < r:
                if w[l] != w[r]:
                    return False
                l, r = l+1, r-1
            return True
        i, j = 0, len(s)-1
        while i<j:
            if s[i] != s[j]:
                return palindrom(s, i, j-1) or palindrom(s, i+1, j)
            i, j = i+1, j-1
        return True
                    