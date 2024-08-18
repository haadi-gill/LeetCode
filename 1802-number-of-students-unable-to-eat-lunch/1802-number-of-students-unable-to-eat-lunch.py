class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        c = Counter(students)
        
        for s in sandwiches:
            if c[s] == 0:
                return c[1] if s == 0 else c[0]
            c[s] -= 1
        
        return c[0] + c[1]