class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        map = {0:1}
        cursum = 0
        res = 0
        for n in nums:
            cursum += n
            div = cursum % k
            if div in map:
                res += map[div]
            map[div] = 1 + map.get(div, 0)
        return res
            
