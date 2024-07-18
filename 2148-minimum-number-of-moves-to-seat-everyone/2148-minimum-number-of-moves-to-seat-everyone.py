class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        diff = 0
        seats = sorted(seats)
        students = sorted(students)

        for i in range(len(seats)):
            diff += abs(seats[i]-students[i])

        return diff