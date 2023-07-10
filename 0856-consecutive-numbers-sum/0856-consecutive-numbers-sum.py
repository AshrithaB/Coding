class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ways = 0
        i = 1
        while n > 0:
            n -= i
            if n%i == 0:
                ways += 1
            i += 1
        return ways
