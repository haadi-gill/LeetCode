'''
521. Longest Uncommon Subsequence I

Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If no such uncommon subsequence exists, return -1.

An uncommon subsequence between two strings is a string that is a
subsequence
of exactly one of them.

 

Example 1:

Input: a = "aba", b = "cdc"
Output: 3
Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
Note that "cdc" is also a longest uncommon subsequence.

Example 2:

Input: a = "aaa", b = "bbb"
Output: 3
Explanation: The longest uncommon subsequences are "aaa" and "bbb".

Example 3:

Input: a = "aaa", b = "aaa"
Output: -1
Explanation: Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a. So the answer would be -1.

 

Constraints:

    1 <= a.length, b.length <= 100
    a and b consist of lower-case English letters.


'''
def findLUSlength(a, b):
    
    max_count = -1
    max_count_a = -1
    max_count_b = -1

    a_s = set()

    for i in range(len(a)+1):
        a_s.add(a[:i])

    a_fs = set(a_s)

    for a_p in a_fs:
        if a_p in b:
            a_s.remove(a_p)
    
            
    b_s = set()

    for i in range(len(b)+1):
        b_s.add(b[:i])

    b_fs = set(b_s)

    for b_p in b_fs:
        if b_p in a:
            b_s.remove(b_p)

    if len(a_s) == 0 and len(b_s) == 0:
        return -1
    
    for a_q in a_s:
        if len(a_q) > max_count_a:
            max_count_a = len(a_q)

    for b_q in b_s:
        if len(b_q) > max_count_b:
            max_count_b = len(b_q)
    
    max_count = max_count_a if max_count_a > max_count_b else max_count_b

    return max_count


def main():
    a = "aefawfawfawfaw"
    b = "aefawfeawfwafwaef"
    print(findLUSlength(a,b))


if __name__ == "__main__":
    main()