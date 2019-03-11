'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''
import collections

class Solution(object):
    def caculator1(self, s):
        i, total, stack = 0, 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i <len(s) and s[i].isdigit():
                    i += 1
                total += stack.pop() * int(s[start:i])
                continue
            if c in "-+(":
                stack += stack[-1] * [1, -1][c == "-"],
            if c == ")":
                stack.pop()
            i += 1
        return total

    def calculate(self, s):
        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            print "c = ", c
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                print "000 i = ", i
                total += signs.pop() * int(s[start:i])
                print "total = ", total, "i = ", i," signs = ", signs
                continue
            if c in '+-(':
                signs += signs[-1] * (1, -1)[c == '-'],
                print "111 total = ", total, "i = ", i," signs = ", signs
            elif c == ')':
                signs.pop()
                print "222 total = ", total, "i = ", i," signs = ", signs
            i += 1
        return total

so = Solution()

s = " 2-1 + 2 "
print so.caculator1(s)