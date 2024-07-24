class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(nums, key=lambda x:reduce(lambda total,i: (total*10)+i, [mapping[g] for g in map(int, str(x))]))