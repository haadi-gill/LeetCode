from collections import defaultdict

class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeroRun = 0
        d = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroRun += 1
            else:
                if zeroRun > 0: d[zeroRun] += 1
                zeroRun = 0

        if zeroRun > 0: d[zeroRun] += 1

        total = 0
        print(d)

        for k,v in d.items():
            for x in range(1,k+1):
                total += (k - x + 1) * v

        return total
