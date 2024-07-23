from collections import defaultdict

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = Counter(nums)

        # print(d)
        # print(d.most_common())
        # print(sorted(d.most_common(), key = lambda x: x[0]))
        # print(sorted(sorted(d.most_common(), key = lambda x: -x[0]), key = lambda x: x[1]))

        a = []

        be = sorted(sorted(d.most_common(), key = lambda x: -x[0]), key = lambda x: x[1])

        for b in be:
            a.extend([b[0]]*b[1])

        # print(a)
        return a