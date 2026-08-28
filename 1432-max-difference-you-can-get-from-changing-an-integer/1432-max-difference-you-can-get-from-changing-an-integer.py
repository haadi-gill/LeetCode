class Solution:
    def maxDiff(self, num: int) -> int:
        string = str(num)
        firstDigit = int(string[0])
        a = 0
        if firstDigit == 9 and len(string) > 1:
            index = 1
            secondDigit = firstDigit
            while index < len(string) and secondDigit == firstDigit:
                secondDigit = int(string[index])
                index += 1
            a = int(string.replace(str(secondDigit), "9"))
        else: 
            a = int(string.replace(str(firstDigit), "9"))

        b = 0
        if firstDigit == 1 and not string.count("1") == len(string):
            index = 1
            secondDigit = firstDigit
            while index < len(string)  and (secondDigit == firstDigit or secondDigit < 1):
                secondDigit = int(string[index])
                index += 1
            b = int(string.replace(str(secondDigit), "0"))
        else:
            b = int(string.replace(str(firstDigit), "1"))

        return  a - b
