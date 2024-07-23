class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = Counter(nums1)#.most_common()
        b = Counter(nums2)#.most_common()

        c = []

        for i in list(set(a).intersection(set(b))):
            c.extend([i]*min(a[i], b[i]))

        return c