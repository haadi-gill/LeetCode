class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sort = sorted(nums)
        count = 0
        
        while(len(sort) > len(set(sort))):
            if sort[0] == sort[1]:
                count += 1
                sort = sort[2:]
            else:
                sort = sort[1:]

        return [count, len(nums)-(2*count)]