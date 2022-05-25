class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total, curSwap = 0, 0
        for n in nums:
            if n == 1:
                total += 1
        for n in nums[:total]:
            if n == 0:
                curSwap += 1
        minSwap = curSwap
        doublenums = nums+nums[:total]
        l = 0
        for r in range(total, len(nums)+total):
            if doublenums[l] == 0:
                curSwap -= 1
            l += 1
            if doublenums[r] == 0:
                curSwap += 1
            minSwap = min(minSwap,curSwap)
        return minSwap