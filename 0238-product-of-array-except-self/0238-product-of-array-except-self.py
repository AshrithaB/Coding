class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        res = [1] * len(nums)
        for i in range(len(nums)-1):
            pre = pre * nums[i]
            res[i+1] = pre
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * post
            post = post * nums[i]
        return res