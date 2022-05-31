class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
        
        '''j,i=0,0
        while i<len(nums):            
            nums[j]=nums[i]
            j+=1
            while nums[i] in nums[i+1:]:
                i+=1
            i+=1
        return(j)'''      
        '''k,u,new=0,0,[]
        for x in nums:
            if x in new:
                u = u+1
            else:
                new.append(x)
                k = k+1
        for i in range(0,u):
            new.append('_')
        for i in range(0,len(nums)):
            nums[i] = new[i]
        return k'''
            
        