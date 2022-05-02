class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n, ans = len(code), []
        if k > 0:
            for j in range(0,n):
                s = 0
                for i in range(j+1,j+k+1):
                    s = s + code[i%n]
                ans.append(s)
        elif k < 0:
            for j in range(0,n):
                s = 0
                for i in range(j-1,j-1+k,-1):
                    s = s + code[i%n]
                ans.append(s)
        else:
            ans = [0]*n
        return ans