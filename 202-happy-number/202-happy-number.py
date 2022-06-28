class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        def next_n(n):
            total_sum = 0
            while n > 0:
                rem = n % 10
                total_sum += rem*rem
                n = n//10
            return total_sum
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = next_n(n)
        return n==1