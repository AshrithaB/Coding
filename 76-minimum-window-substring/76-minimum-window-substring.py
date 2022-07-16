class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        window, countT = {}, {}
        for w in t:
            countT[w] = 1 + countT.get(w, 0)
        have, need = 0, len(countT)
        res, reslength = [-1, -1], float('infinity')
        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)
            if ch in countT and window[ch] == countT[ch]:
                have += 1
            while have == need:
                if r-l+1 < reslength:
                    res = [l, r]
                    reslength = r-l+1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if reslength != float('infinity') else ""
        
                
            
        
            