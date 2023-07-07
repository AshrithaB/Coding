class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixhash = {0:1}
        subarray = 0
        cursum = 0
        for n in nums:
            cursum += n
            div = cursum % k
            subarray += prefixhash.get(div, 0)
            prefixhash[div] = 1 + prefixhash.get(div, 0)
        return subarray