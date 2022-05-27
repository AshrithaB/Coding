class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num>0:
            if num & 1:
                num = num ^ 1
            else:
                num = num>>1
            step += 1
        return step
    
    
    