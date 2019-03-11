'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

from collections import Counter
import string


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return 0
        for i in range(len(s)):   # here we need to tranverse all the letter in s
            print "i=",i
            print "s[i] = ",s[i],"s[i+1] = ",s[i+1:]
            if s[i] not in (s[:i]+s[i+1:]):
                return i
        return -1
    
    def firstUniqChar2(self, s):
        letters = string.ascii_letters
        index = [s.index(l) for l in letters if Counter(s)[l] == 1]
        return min(index) if len(index) > 0 else -1


s = Solution()
str = "dddccdbba"

print s.firstUniqChar2(str)