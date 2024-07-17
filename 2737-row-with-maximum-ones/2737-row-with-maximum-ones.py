class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxOnes = 0
        pos = 0

        for i in range(len(mat)):
            if mat[i].count(1) > maxOnes:
                maxOnes = mat[i].count(1)
                pos = i

        return [pos, maxOnes]