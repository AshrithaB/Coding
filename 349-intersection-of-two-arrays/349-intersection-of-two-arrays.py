class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        for n in nums1:
            if n in nums2:
                seen.add(n)
        return seen