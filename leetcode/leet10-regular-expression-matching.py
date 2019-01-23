#-*- coding: utf-8

'''
* 代表匹配0个或者多个前面的字符，所以出现*之前必须有字符
. 代表匹配一个任意字符
s could be empty and contains only lowercase letters a-z
p could be empty and contains only lowercase letters a-z, and character like . or *

'''

'''
思路：递归或者DP。
递归：
1.如果s[0] == p[0] 或者p[0] == "."记下first_match = True, 否则first_match = False
2. 继续处理下一个字符，如果下一个字符不为*, 则处理isMatch(s[1:], p[1:])
3. 如果p[1] == "*",如果first_match匹配， 则继续看isMatch(s[1:], p)是否继续匹配；如果first_match不匹配，由于*可以表示0个字符，则看isMatch(s, p[2:])是否匹配

'''

class Solution(object):
	def isMatch(self, s, p):
		'''
		type： s str
		type: p str
		return bool
		'''
		if len(s) == 0 and len(p) == 0:
			return True
		first_match = False
		if len(s) > 0 and len(p) > 0 :
			first_match = p[0] in [s[0], '.']
		if len(p) >= 2 and p[1] == '*':
			return (first_match and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
		else:
			return first_match and self.isMatch(s[1:], p[1:])


if __name__ == '__main__':
    s = 'aab'
    p = 'c*a*b'
    so = Solution()
    ret = so.isMatch(s,p)
    print "ret=",ret