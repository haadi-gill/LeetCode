class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        single = {
            0:"",
            1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine"
        }

        tens = {
            2:"Twenty",
            3:"Thirty",
            4:"Forty",
            5:"Fifty",
            6:"Sixty",
            7:"Seventy",
            8:"Eighty",
            9:"Ninety"
        }

        elevens = {
            0:"Ten",
            1:"Eleven",
            2:"Twelve",
            3:"Thirteen",
            4:"Fourteen",
            5:"Fifteen",
            6:"Sixteen",
            7:"Seventeen",
            8:"Eighteen",
            9:"Nineteen"
        }

        digits = []

        curr = num

        while curr > 0:
            digits.insert(0,curr%10)
            curr = curr // 10
        
        # print(digits)

        s = ""

        if (len(digits) >= 10):
            s += single[digits[0]] + ' Billion'
            digits.pop(0)
            if (sum(digits) != 0):
                s += " "
        
        if (len(digits) == 9):
            if digits[0] != 0:
                s += single[digits[0]] + " Hundred "
                if (sum(digits[1:3]) == 0):
                    digits.pop(0)
                    digits.pop(0)
                    s += "Million "
            digits.pop(0)
            if (sum(digits) == 0):
                return s.strip()

        if (len(digits) == 8):
            if digits[0] == 1:
                s += elevens[digits[1]]
                digits.pop(0)
                digits.pop(0)

            elif digits[0] == 0:
                s += single[digits[1]]
                digits.pop(0)
                digits.pop(0)
            else:
                s += tens[digits[0]] 
                if digits[1] != 0:
                    s += " " + single[digits[1]]
                digits.pop(0)
                digits.pop(0)
            if not(s.strip().endswith('Billion')):
                s += " Million "
        
        if (len(digits) == 7):
            s += single[digits[0]]
            digits.pop(0)
            s += " Million "




        if (len(digits) == 6):
            if digits[0] != 0:
                s += single[digits[0]] + " Hundred "
                if (sum(digits[1:3]) == 0):
                    digits.pop(0)
                    digits.pop(0)
                    s += "Thousand "
            digits.pop(0)
            if (sum(digits) == 0):
                return s.strip()

        if (len(digits) == 5):
            if digits[0] == 1:
                s += elevens[digits[1]]
                digits.pop(0)
                digits.pop(0)

            elif digits[0] == 0:
                s += single[digits[1]]
                digits.pop(0)
                digits.pop(0)
            else:
                s += tens[digits[0]]
                if digits[1] != 0:
                    s += " " + single[digits[1]]
                digits.pop(0)
                digits.pop(0)
            if not(s.strip().endswith('illion')):
                s += " Thousand "
        
        if (len(digits) == 4):
            s += single[digits[0]]
            digits.pop(0)
            s += " Thousand "



        if (len(digits) == 3):
            if digits[0] != 0:
                s += single[digits[0]] + " Hundred "
                if (sum(digits[1:]) == 0):
                    digits.pop(0)
                    digits.pop(0)
            digits.pop(0)

        if (len(digits) == 2):
            if digits[0] == 1:
                s += elevens[digits[1]]
                digits.pop(0)
                digits.pop(0)

            elif digits[0] == 0:
                s += single[digits[1]]
                digits.pop(0)
                digits.pop(0)
            else:
                s += tens[digits[0]]
                if digits[1] != 0:
                    s += " " + single[digits[1]]
                digits.pop(0)
                digits.pop(0)
            s += " "
        
        if (len(digits) == 1):
            s += single[digits[0]] 
            digits.pop(0)
            s += " "


        return(s.strip())