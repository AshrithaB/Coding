class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        subarray = 0
        hashmap = {0:1}
        for n in nums:
            subarray += n
            div = subarray % k
            res += hashmap.get(div, 0)
            hashmap[div] = 1 + hashmap.get(div, 0)
        return res
