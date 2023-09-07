class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        maxchar = 0
        store = {}
        l = 0
        for r in range(len(s)):
            store[s[r]] = 1 + store.get(s[r], 0)
            maxchar = max(maxchar, store[s[r]])
            while l<=r and r-l+1-maxchar > k:
                maxlen = max(maxlen, r-l)
                store[s[l]] -= 1
                if store[s[l]] == 0:
                    del store[s[l]]
                l += 1
        maxlen = max(maxlen, r-l+1)
        return maxlen