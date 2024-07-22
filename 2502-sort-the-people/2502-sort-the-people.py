class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        heights = sorted([(h, i) for i,h in enumerate(heights)], reverse=True)

        ordered = []

        for _,i in heights:
            ordered.append(names[i])

        return ordered