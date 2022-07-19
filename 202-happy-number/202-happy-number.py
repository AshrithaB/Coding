class Solution:
    def isHappy(self, n: int) -> bool:
        def getn(num):
            res = 0
            while num:
                rem = num%10
                res = res + (rem*rem)
                num = num//10
            return res
            
            
        slow = n
        fast = getn(n)
        while slow != fast and fast != 1:
            slow = getn(slow)
            fast = getn(getn(fast))
        return fast == 1