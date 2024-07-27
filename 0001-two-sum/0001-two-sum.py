class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        previous = {}
        for i in range(n):
            difference = target - nums[i]
            if difference in previous:
                return [previous[difference], i]
            else:
                previous[nums[i]] = i

