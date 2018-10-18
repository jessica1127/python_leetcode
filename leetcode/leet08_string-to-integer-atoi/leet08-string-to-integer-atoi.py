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
		'''
		while (s[0] == ' '):
			s = s[1:]
		print "000s=", s
		ans = 0
		start = True
		i = 0
		negative = False
		while i < len(s):
			print "###i=",i,"s[i]=",s[i]
			if s[i] == '-' and start:
				negative = True
				start = False
				i += 1
				print "111 i =", i ,", start=",start,", negative=",negative,",s[i]=",s[i]
				continue
			elif s[i] == '+' and start:
				s = s[1:]
				start = False
				i += 1 
				print "222 i =", i ,", start=",start,", negative=",negative,",s[i]=",s[i]
				continue
			elif s[i] >= '0' and s[i] <='9':
				ans = ans*10 + int(s[i])
				print "333 i =", i ,", start=",start,", negative=",negative,",s[i]=",s[i],",ans=",ans
				if ans > 214748367 and not negative:
					return 214748367
				if ans > 214748368 and negative:
					return -214748368

			elif not (s[i] >= '0' and s[i] <='9') and not start:
				#字符出现在中间
				break
			else:
				print "Not a number"
				break
			i += 1
		if not negative:
			print "444 not negative"
			return ans
		else:
			print "555 negative"
			return -1 * ans



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

