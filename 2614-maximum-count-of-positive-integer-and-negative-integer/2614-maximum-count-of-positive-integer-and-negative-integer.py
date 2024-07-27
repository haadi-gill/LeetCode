class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(len([a for a in nums if a < 0]), len([a for a in nums if a > 0]))