#-*- coding: utf-8

'''
* 代表匹配0个或者多个前面的字符
. 代表匹配一个任意字符
s could be empty and contains only lowercase letters a-z
p could be empty and contains only lowercase letters a-z, and character like . or *

'''

'''
思路：递归
1）如果p的下一个字符是*：如果p和s当前的字符相同或者p当前是., 则p一直往右移动知道p没有出现.或者x*这样的情况，x是指跟s相同的字符
2）如果p的下一个字符不是*：如果p和s当前的字符相同或者p当前字符是., 则p和s往右移动一个字符，递归
'''

class Solution(object):
	def isMatch(self, s, p):
		'''
		type： s str
		type: p str
		return bool
		'''
		sLen = len(s)
		pLen = len(p)
		if pLen == 0:
			return sLen == 0
		if pLen == 1:
			if p ==s or p == '.' and sLen == 1:
				return True
			else:
				return False
		#p的最后一个字符不是* 或者.且不出现在s里面，则return False
		if p[-1] != '*' or p[-1] != '.' and p[-1] not in s:
			return False
		if p[1] != '*':
			if len(s) > 0 and p[0] == s[0] or p[0] == '.':
				return self.isMatch(s[1:], p[1:])
			return False

		else:
			while (len(s) > 0) and p[0] == s[0] or p[0] == '.':
				if self.isMatch(s, p[2:]):
					return True
				s = s[1:]
			return self.isMatch(s, p[2:])




if __name__ == '__main__':
    s = 'abc'
    p = '*'
    so = Solution()
    ret = so.isMatch(s,p)
    print "ret=",ret