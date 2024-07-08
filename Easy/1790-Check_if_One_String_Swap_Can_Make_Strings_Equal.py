'''
1790. Check if One String Swap Can Make Strings Equal

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

 

Constraints:

    1 <= s1.length, s2.length <= 100
    s1.length == s2.length
    s1 and s2 consist of only lowercase English letters.


'''

def areAlmostEqual(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    s1 = str(s1)
    s2 = str(s2)
    diffIndex = -1
    # if [c for c in s1].sort() != [c for c in s2].sort(): return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if diffIndex == -1:
                diffIndex = i
            else:
                s1 =  s1[:diffIndex] + s1[i] + s1[diffIndex+1:i] + s1[diffIndex] + s1[i+1:]
                break
    return s1 == s2  