class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        totalOnes = nums.count(1)
        curZeros = 0
        for i in range(totalOnes):
            if nums[i] == 0:
                curZeros += 1
        minSwap = curZeros
        doublenums = nums+nums[:totalOnes]
        n = len(doublenums)
        for r in range(totalOnes, n):
            if doublenums[r-totalOnes] == 0:
                curZeros -= 1
            if doublenums[r] == 0:
                curZeros += 1
            minSwap = min(minSwap,curZeros)
        return minSwap
        '''total, curSwap = 0, 0
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
        return minSwap'''