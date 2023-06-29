class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits): return []
        digitlettermap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        def dfs(i, s):
            if len(s) == len(digits):
                res.append(s)
                return
            for j in digitlettermap[digits[i]]:
                dfs(i+1, s + j)
        if digits:
            dfs(0, "")
        return res