class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c = Counter(arr)
        return len(set([a for v,a in c.items()])) == len([a for v,a in c.items()])