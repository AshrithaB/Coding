class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0:1}
        cursum = 0
        res = 0
        for n in nums:
            cursum += n
            if cursum-k in map:
                res += map[cursum-k]
            map[cursum] = 1 + map.get(cursum, 0)
        return res