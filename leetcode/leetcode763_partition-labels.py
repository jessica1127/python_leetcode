'''
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
'''

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dic = {}
        for i, c in enumerate(S):
            dic[c] = i
        print "S= ", S
        print "dic = ", dic
        
        cur_max = 0
        res = []
        count = 0
        
        for i, c in enumerate(S):
            count += 1
            cur_max = max(cur_max, dic[c])
            
            if cur_max == i:
                res.append(count)
                count = 0
        return res


S = "ababcbacadefegdehijhklij"
s = Solution()
print s.partitionLabels(S)