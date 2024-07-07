'''
278. First Bad Version


You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:

Input: n = 1, bad = 1
Output: 1

 

Constraints:

    1 <= bad <= n <= 231 - 1


'''
import math

def isBadVersion(n):
    #return n >= 1702766719
    return n >= 2


def firstBadVersion(n):
    i = 1
    j = n

    if isBadVersion(i):
        return i

    while(i < j):
        print(f"i: {i} j: {j}")

        mid = math.floor((i+j)/2)

        if (isBadVersion(mid)):
            j = mid 
        else:
            i = mid + 1





        # if isBadVersion(i):
        #     i = j
        #     j = math.ceil((n+j)/2)
        # elif isBadVersion(j):
        #     j = math.ceil((i+j)/2)
        # else:
        #     j = math.ceil((n+j)/2)
        
    return i

def main():
    #print(firstBadVersion(2126753390))
    print(firstBadVersion(3))


if __name__ == "__main__":
    main()