class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
     
        matches = []
        nextVal = 0
        for i, w in enumerate(words):
            matches.append(nextVal)

            if w[0] in vowels and w[-1] in vowels:
                nextVal = matches[i] + 1
            
        
        matches.append(nextVal)

        

        output = []

        for q in queries:
            # if q[0] == 0:
            #     output.append(matches[q[1]] - matches[q[0]]+1)
            # else:
            output.append(matches[q[1]+1] - matches[q[0]])   
        return output
            