class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        ans = set()
        for n in set(nums2):
            if n in seen:
                ans.add(n)
        return ans