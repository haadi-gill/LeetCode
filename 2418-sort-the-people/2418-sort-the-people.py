class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        test = []
        for i in [i for (i, a) in sorted(enumerate(heights), key= lambda x: x[1], reverse=True)]:
            test.append(names[i])
        return test