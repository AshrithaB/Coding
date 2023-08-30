class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            if target - numbers[i] in numbers:
                l = i
                r = len(numbers)-1
                while l<r:
                    total = numbers[l] + numbers[r]
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        return [l+1,r+1]