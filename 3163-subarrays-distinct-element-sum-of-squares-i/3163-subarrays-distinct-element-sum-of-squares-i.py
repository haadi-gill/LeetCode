class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)+1):
                a = nums[i:j]
                total += len(set(a))**2

        return total