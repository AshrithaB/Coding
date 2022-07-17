class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j = m-1, n-1
        index = m+n-1
        while i > -1 and j > -1:
            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1
        while j > -1:
            nums1[index] = nums2[j]
            j -= 1
            index -= 1
        return
        