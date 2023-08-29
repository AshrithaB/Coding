class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        op = 0
        hashmap = {}
        for n in nums:
            if n < k:
                if k-n in hashmap:
                    op += 1
                    hashmap[k-n] -= 1
                    if hashmap[k-n] == 0:
                        del hashmap[k-n]
                else:
                    hashmap[n] = 1 + hashmap.get(n, 0)
        return op
