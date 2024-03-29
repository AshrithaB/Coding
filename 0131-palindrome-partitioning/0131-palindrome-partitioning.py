class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [list(s)]
        res = []
        part = []
        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return 
            for j in range(i, len(s)):
                if self.ispali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
    
    def ispali(self, char, l, r):
        while l <= r:
            if char[l] != char[r]:
                return False
            l += 1
            r -= 1
        return True