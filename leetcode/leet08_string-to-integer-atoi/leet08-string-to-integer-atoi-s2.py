import re 

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        m = re.search('^\s*([+-]?[0-9]+)', str)
        try:
            i = int(m.group(1))
            return max(min(i, 2147483647), -2147483648)
        except AttributeError as e:
            return 0

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