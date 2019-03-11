'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

'''



class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        dp = [0]*(len(s)+1)
        dp[0] = 1
        #print "len(s)+1 =", len(s)+1
        for i in range(1, len(s)+1):
            for j in range(i):
                #print "i = ", i, " j = ", j, " dp[j] = ", dp[j], " s[j:i] = ", s[j:i]
                if dp[j] == 1 and s[j:i] in wordSet:
                    dp[i] = 1
                    #print "111 dp = ", dp
                    break
                else:
                    dp[i] = 0
                #print "000 dp = ", dp
        #print "dp[-1] = ", dp[-1]
        return dp[-1] == 1
        

if __name__ == '__main__':
    so = Solution()
    s = "leetcode"
    wordDict = ["leet", "code", "le"]
    print so.wordBreak(s, wordDict)

    # s2 = "applepenapple"
    # wordDict2 = ["apple", "pen"] 
    # print so.wordBreak(s2, wordDict2)















