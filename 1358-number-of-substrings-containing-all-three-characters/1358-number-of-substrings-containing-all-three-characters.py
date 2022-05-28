class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def atmost(k: int)-> int:
            seen = {}
            res = 0
            l = 0
            for r in range(len(s)):
                seen[s[r]] = 1 + seen.get(s[r], 0)
                while len(seen) > k:
                    seen[s[l]] -= 1
                    if seen[s[l]] == 0:
                        del seen[s[l]]
                    l += 1
                res += r-l+1
            return res
        return atmost(3) - atmost(2)
        