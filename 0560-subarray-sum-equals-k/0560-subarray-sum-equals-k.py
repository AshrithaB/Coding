class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray = 0
        prefixhash = {0:1}
        l = 0
        cursum = 0
        for r in range(len(nums)):
            cursum += nums[r]
            if cursum - k in prefixhash:
                subarray += prefixhash[cursum - k]
            if cursum not in prefixhash:
                prefixhash[cursum] = 0
            prefixhash[cursum] += 1 
        return subarray