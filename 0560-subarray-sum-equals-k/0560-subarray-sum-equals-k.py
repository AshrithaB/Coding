class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray = 0
        prefixhash = {0:1}
        l = 0
        cursum = 0
        for r in range(len(nums)):
            cursum += nums[r]
            subarray += prefixhash.get(cursum-k, 0)
            prefixhash[cursum] = 1 + prefixhash.get(cursum, 0)
        return subarray