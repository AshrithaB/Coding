class Solution:
    def validPalindrome(self, s: str) -> bool:
        def pali(s, l, r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True
        l, r = 0, len(s)-1    
        while l<r:
            if s[l]!=s[r]:
                return pali(s, l, r-1) or pali(s, l+1,r)
            l, r = l+1, r-1
        return True