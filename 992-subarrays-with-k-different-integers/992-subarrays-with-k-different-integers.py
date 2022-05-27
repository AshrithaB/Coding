class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarrayWithAtmostK(K: int) -> int:
            seen = {}
            ans = 0
            l = 0
            for r in range(len(nums)):
                seen[nums[r]] = 1 + seen.get(nums[r], 0)
                while len(seen) > K:
                    seen[nums[l]] -= 1
                    if seen[nums[l]]==0:
                        del(seen[nums[l]])
                    l += 1
                ans += r-l+1
            return ans
        return subarrayWithAtmostK(k) - subarrayWithAtmostK(k-1)       
            
        