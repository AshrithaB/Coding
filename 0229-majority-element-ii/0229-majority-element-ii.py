class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = math.floor(len(nums)/3)
        res = set()
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            if count[n] > l:
                res.add(n)
        return list(res)

            
