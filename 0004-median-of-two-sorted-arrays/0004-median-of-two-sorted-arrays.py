class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        A, B = nums1, nums2 
        
        if len(nums1) > len(nums2):
            A,B =  nums2, nums1

        total = len(A) + len(B)
        half = total // 2

        l = 0
        r = len(A)-1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if i+1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if j+1 < len(B) else float("infinity")
            
            # print("i", i,"j",j)
            # print("Aleft", Aleft,"Aright", Aright)
            # print("Bleft", Bleft,"Bright", Bright)

            if Aleft <= Bright and Aright >= Bleft:
                if total % 2:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft, Bleft)+min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

        