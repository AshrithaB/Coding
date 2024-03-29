class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i,j = 0, len(nums)-1
        res = []
        while i<=j:
            if abs(nums[i]) > abs(nums[j]):
                res.append(nums[i]*nums[i])
                i += 1
            else:
                res.append(nums[j]*nums[j])
                j -= 1
        return res[::-1]