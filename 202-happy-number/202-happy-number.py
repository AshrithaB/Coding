class Solution:
    def isHappy(self, n: int) -> bool:
        def next_n(n):
            total_sum = 0
            while n > 0:
                rem = n % 10
                total_sum += rem*rem
                n = n//10
            return total_sum
        slow = n
        fast = next_n(n)
        while fast != 1 and slow != fast:
            slow = next_n(slow)
            fast = next_n(next_n(fast))
        return fast == 1