class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        resstr = ""
        tcount, scount = {},{}
        for i in range(len(t)):
            tcount[t[i]] = 1 + tcount.get(t[i], 0)
            scount[s[i]] = 1 + scount.get(s[i], 0)
        have, need = 0, len(tcount)
        res = [float('inf'), [-1, -1]]
        for k, v in scount.items():
            if k in tcount and scount[k] >= tcount[k]:
                have += 1
        if have == need:
            return s[:len(t)]
        l = 0
        r = 0
        for r in range(len(t), len(s)):
            scount[s[r]] = 1 + scount.get(s[r], 0)
            if s[r] in tcount and scount[s[r]] == tcount[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < res[0]:
                    res = [r-l+1, [l, r+1]]
                scount[s[l]] -= 1
                if s[l] in tcount and scount[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1   
        return "" if res[0] == float('inf') else s[res[1][0]:res[1][1]]
