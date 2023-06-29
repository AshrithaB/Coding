class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits): return []
        digitlettermap = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        res = []
        def dfs(i, s):
            if i == len(digits):
                res.append(''.join(s))
                return
            for j in range(len(digitlettermap[digits[i]])):
                s.append(digitlettermap[digits[i]][j])
                dfs(i+1, s)
                s.pop()
        
        dfs(0, [])
        return res