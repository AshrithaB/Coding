class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s = {}
        for ch in s:
            counter_s[ch] = 1 + counter_s.get(ch, 0)
        counter_t = {}
        for ch in t:
            counter_t[ch] = 1 + counter_t.get(ch, 0)
            if ch in counter_s and counter_t[ch] > counter_s[ch]:
                return False
        return counter_s == counter_t