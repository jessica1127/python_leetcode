#/usr/bin/env python
#-*- coding=utf-8
from collections import defaultdict
'''
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

time: O(n)
'''
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = defaultdict(list)
        restmp = []
        result = []
        for i, char in enumerate(S):
            # print "i= ",i, " char= ",char
            if char == C:
                res[i] = 0
                restmp.append(i)

        for i, char in enumerate(S):
            if char != C:
                res[i] = min(abs(i - indexC) for indexC in restmp)

        #print "res==", res
        for i in xrange(len(res)):
            result.append(res[i])
        return result

if __name__ == '__main__':
    S = "loveleetcode"
    C = 'e'
    s = Solution()
    result = s.shortestToChar(S, C)
    print "result = ", result




