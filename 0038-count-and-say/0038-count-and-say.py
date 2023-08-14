class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        def say(s):
            l = list(s)
            res = []
            i = 0
            while i < len(l):
                c = 1
                while i+1 < len(l) and l[i] == l[i+1]:
                    i += 1
                    c += 1
                res.append(str(c)+l[i])
                i += 1
            return ''.join(res)
        return say(self.countAndSay(n-1))
