class Solution(object):
	def myAtoi(self, strin):
		'''
		type: 
		str: str
		rtype: int
		'''
		strin = strin.strip()
		print "strin[0]=",strin[0]
		if strin[0] == '-' or strin[0] in range(0,10):
			for i in strin:
				if not (i in range(0,10)):
					tmpindex = strin.index(i)
					strin = strin[0:tmpindex+1]
					break
			ret = int(strin)
			if ret >= 2147483647:
				return 2147483647
			elif ret <= -2147483648:
				return -2147483648
			else:
				return ret

		else:
			return 0


if __name__ == '__main__':
	s1 = "42"
	s2 = "     -42"
	s3 = "4193 with words"
	s4 = "words and 987"
	s5 = "-91283472332"
	so = Solution()
	ret_s1 = so.myAtoi(s1)
	print "ret_s1=",ret_s1

