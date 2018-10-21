#-*-coding: utf-8
'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

class Solution(object):
	def isPalindrome(self, x):
		'''
		type x: int
		rtype: bool
		'''
		x = str(x)
		ret = True
		if len(x) == 0:
			return ret
		if x == x[::-1]:
			return ret
		else:
			return False

if __name__ == '__main__':
	so = Solution()
	x1 = '121'
	x2 = '-121'
	x3 = '10'
	ret1 = so.isPalindrome(x1)
	ret2 = so.isPalindrome(x2)
	ret3 = so.isPalindrome(x3)
	print "ret1=",ret1,",ret2=",ret2,",ret3=",ret3