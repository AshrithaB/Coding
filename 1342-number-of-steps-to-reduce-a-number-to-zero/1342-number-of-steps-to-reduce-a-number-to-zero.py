class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = num==0
        while num>0:
            step += 1 + (num & 1)
            num >>= 1
        return step - 1
        '''step = 0
        while num>0:
            if num & 1:
                num = num ^ 1
            else:
                num = num>>1
            step += 1
        return step'''
        '''step = 0
        while num>0:
            if num%2 == 0:
                num = num//2
            else:
                num -= 1
            step += 1
        return step'''
    
    
    