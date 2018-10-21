#-*- coding: utf-8
class Solution(object):
	def myAtoi(self, s):
		'''
		type: 
		str: str
		rtype: int
		'''
		'''
		去掉开头的空格
		1) 以空格开头的去掉空格
		2) 以+-号开头的，按照正负数，
		3) 其他符号，非0-9且非start的，退出循环
		'''
		if len(s) == 0 :
			return 0
		i = 0
		positive = True #正数
		start = True
		sigStartFlag = True
		ans = 0
		while i < len(s):
			if s[i] != ' ':
				start = False
			elif s[i] == ' ' and start:
				i += 1
				continue
			elif sigStartFlag:
				if s[i] == '-':
					positive = False
					i += 1
					sigStartFlag = False
				elif s[i] == '+':
					i += 1
					sigStartFlag = False
			elif s[i] >= '0' and s[i] <= '9':
				ans = 10*ans + s[i]
				if ans > 2147483647 and positive:
					return 2147483647
				elif ans > 2147483648 and not positive:
					return -2147483647
			else:
				break
			i += 1
		if positive:
			return ans
		else:
			return -1*ans



if __name__ == '__main__':
	s1 = "42"
	s2 = "     -42   "
	s3 = "4193 with words"
	s4 = "words and 987"
	s5 = "-91283472332"
	so = Solution()
	ret_s1 = so.myAtoi(s1)
	print "ret_s1=",ret_s1
	ret_s2 = so.myAtoi(s2)
	print "ret_s2=",ret_s2
	ret_s3 = so.myAtoi(s3)
	print "ret_s3=",ret_s3
	ret_s4 = so.myAtoi(s4)
	print "ret_s4=",ret_s4