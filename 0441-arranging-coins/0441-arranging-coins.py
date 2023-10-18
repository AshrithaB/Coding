class Solution:
    def arrangeCoins(self, n: int) -> int:
        for i in range(1, math.ceil(n/2)+2):
            n = n - i
            if n < 0:
                return i-1
            elif n == 0:
                return i
        


        