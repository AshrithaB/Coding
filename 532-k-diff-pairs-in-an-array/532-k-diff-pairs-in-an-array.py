class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, 1
        count = 0
        while j < len(nums) and i < j:
            if nums[j] - nums[i] == k:
                count += 1
                i += 1
                j += 1
                while j < len(nums) and nums[j] == nums[j-1]:
                    j += 1
            elif nums[j] - nums[i] < k:
                j += 1
            elif nums[j] - nums[i] > k:
                i += 1
                if j - i == 0:
                    j += 1
        return count
        