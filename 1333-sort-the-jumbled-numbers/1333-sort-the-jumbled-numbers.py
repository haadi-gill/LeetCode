m = []

def translate(n):
    return reduce(lambda total,i: (total*10)+i, [m[g] for g in map(int, str(n))])


class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # global m 
        # m = mapping
        # return sorted(nums, key=lambda x:translate(x))
        return sorted(nums, key=lambda x:reduce(lambda total,i: (total*10)+i, [mapping[g] for g in map(int, str(x))]))