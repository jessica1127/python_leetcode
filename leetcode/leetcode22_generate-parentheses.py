'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
reference: https://www.youtube.com/watch?v=XF0wh8M2A6E
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #item is the current string
        def helper(left, right, item, result):
            #if used right parenthsis > used left parenthsis, we should return. it is wrong item, eg: (()) )... ...
            print "left = ", left, "right = ", right, "item = ", item, "result = ", result
            if right < left:
                return 
            # if left = right =0 , we should append current item to result
            if left == 0 and right ==0:
                print 111
                result.append(item) 
            
            if left > 0 :
                print 222
                helper(left-1, right, item + "(", result)
            if right > 0:
                print 333
                helper(left, right-1, item + ")", result)
           


        if n == 0:
            return []
        result = []
        # "" is the current string contains the parentheses
        helper(n, n, "", result)
        return result


s = Solution()
n = 3
print s.generateParenthesis(n)