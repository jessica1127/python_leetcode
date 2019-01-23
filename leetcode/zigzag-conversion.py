#-*-coding:utf-8
'''
给出：“PAYPALISHIRING”， numRows=3
即：
P   A   H   N
A P L S I I G
Y   I   R
输出： PAHNAPLSIIGYIR

'''
class Solution(object):
    def convert(self, s, numRows):
        size = len(s)
        if size <= numRows or numRows == 1:
            return s
        i = 0
        ans = ""
        while i < numRows:
            j = i
            if i == 0 or i == numRows-1:
                while j < size:
                    ans += s[j]
                    j += 2*numRows -2
                    print "00 i=,",i,",j=",j,",ans=",ans
                    if 2*numRows -2 == 0:
                        break
            else:
                while j < size:
                    ans += s[j]
                    j += 2*(numRows - i) -2
                    
                    if j >= size:
                        break
                    ans += s[j]
                    j += 2*i
                    print "11 i=,",i,",j=",j,",ans=",ans
            i += 1
        return ans

if __name__ == '__main__':
    s = "krvlceroztrzycuyovcakvfswgkgszhcscpuhhigcchceedszhujczdaiohapocirreaapicrrfxviruplgtljvtzcvrtxbm"

    ret_s = Solution().convert(s, 3)
    print "ret_s=", ret_s