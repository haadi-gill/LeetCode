class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for a in range(numRows):
            if a < 2:
                triangle.append([1]*(a+1))
            else:
                temp = [1]
                for b in range(1, a):
                    temp.append(triangle[a-1][b-1] + triangle[a-1][b])
                temp.append(1)
                triangle.append(temp)

        return triangle

        return triangle
