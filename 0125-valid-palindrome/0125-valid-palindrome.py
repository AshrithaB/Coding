class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        alphanum = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        while l <= r:
            while l < r and s[l] not in alphanum:
                l += 1
            while l < r and s[r] not in alphanum:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

        