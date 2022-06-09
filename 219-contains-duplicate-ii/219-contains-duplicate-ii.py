class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, r in enumerate(nums):
            if r in seen and abs(seen[r]-i)<=k:
                return True
            seen[r] = i
        return False
        