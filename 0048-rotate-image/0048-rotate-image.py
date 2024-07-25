class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Transpose
        for a in range(len(matrix)):
            for b in range(a+1, len(matrix[a])):
                print(a, b,matrix[a][b], matrix[b][a])
                matrix[a][b], matrix[b][a] = matrix[b][a] , matrix[a][b]  


        # Reflect

        for i in range(len(matrix)):
            for j in range(len(matrix[i])//2):
                matrix[i][j], matrix[i][len(matrix)-j-1] = matrix[i][len(matrix)-j-1], matrix[i][j]
