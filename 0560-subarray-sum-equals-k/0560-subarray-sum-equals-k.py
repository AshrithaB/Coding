class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cursum = 0
        res = 0
        hashmap = {0:1}
        for n in nums:
            cursum += n
            res += hashmap.get(cursum-k, 0)
            hashmap[cursum] = 1 + hashmap.get(cursum, 0)
        return res