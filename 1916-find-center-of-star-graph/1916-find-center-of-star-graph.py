class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        o = []
        for e in edges:
            o.extend(e)

        return(Counter(o).most_common()[0][0])