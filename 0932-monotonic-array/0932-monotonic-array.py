class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        else:
            target = ""
            if nums[0] < nums[1]:
                target = "inc"  
            elif nums[0] > nums[1]:
                target = "dec"
            if target == "inc":
                i = 1
                while i < len(nums) and nums[i-1] <= nums[i]:
                    i += 1
            elif target == "dec":
                i = 1
                while i < len(nums) and nums[i-1] >= nums[i]:
                    i += 1
            else:
                i = 1
                while i < len(nums) and nums[i-1] == nums[i]:
                    i += 1
                if i == len(nums): 
                    return True
                target = "inc" if nums[i-1] < nums[i] else "dec"
                if target == "inc":
                    while i < len(nums) and nums[i-1] <= nums[i]:
                        i += 1
                elif target == "dec":
                    while i < len(nums) and nums[i-1] >= nums[i]:
                        i += 1
        return True if i == len(nums) else False
