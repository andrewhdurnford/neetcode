class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = (total) // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            m1 = (l + r) // 2
            m2 = half - m1 - 2
            
            Al = A[m1] if m1 >= 0 else -1000001
            Ar = A[m1 + 1] if m1 < (len(A) - 1) else 1000001
            Bl = B[m2] if m2 >= 0 else -1000001
            Br = B[m2 + 1] if m2 < (len(B) - 1) else 1000001

            if Al <= Br and Bl <= Ar:
                if total % 2:
                    return min(Ar, Br)
                else:
                    return (max(Al, Bl) + min(Ar, Br)) / 2
            elif Br < Al:
                r = m1 - 1
            else:
                l = m1 + 1
                