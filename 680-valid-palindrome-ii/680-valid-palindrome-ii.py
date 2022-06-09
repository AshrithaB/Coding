class Solution:
    def validPalindrome(self, s: str) -> bool:
        def pali(sub: str) -> bool:
            i, j = 0, len(sub)-1
            while i<j:
                if sub[i] != sub[j]:
                    return False
                i, j = i+1, j-1
            return True
        
        l, r = 0, len(s)-1
        k = 0
        while l<r:
            if s[l] != s[r]:
                return pali(s[l+1:r+1]) or pali(s[l:r])
            l, r = l+1, r-1
        return True
        
        