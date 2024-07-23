from collections import defaultdict

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        out = []

        for k,v in sorted(d.items(), key=lambda item: (item[1], -item[0])):
 
            out += [k for i in range(v)]
        
        # print(sorted(d.items(), key=lambda item: (item[1], -item[0])))
        # print(out)
        return out