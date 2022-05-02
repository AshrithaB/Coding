class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []: return []
        elif len(nums) == 1: return [str(nums[0])]
        final, i, k = [], 0, 0
        while i<max(nums):
            start = nums[k]
            i = start
            while i!=max(nums) and nums[k+1]==i+1:
                i = i+1
                k = k+1
            end = nums[k]
            k = k+1
            if start==end:
                final.append(str(start))
            else:
                final.append(str(str(start)+"->"+str(end)))
        return final
                
        