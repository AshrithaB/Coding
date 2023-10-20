class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(A) + len(B)
        half = total//2
        if len(A) > len(B):
            A, B = B, A
        s, e = 0, len(A)-1
        while True:
            m1 = (s+e)//2
            m2 = half-m1-2
            Aleft = A[m1] if m1 > -1 else float("-inf")
            Aright = A[m1+1] if m1+1 < len(A) else float("inf")
            Bleft = B[m2] if m2 > -1 else float("-inf")
            Bright = B[m2+1] if m2+1 < len(B) else float("inf") 
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                e = m1 - 1
            else:
                s = m1 + 1
