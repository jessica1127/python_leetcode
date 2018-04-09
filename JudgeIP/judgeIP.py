#coding:utf-8
'''
代码实现使用基础语言实现，判断IP合法性：
例如：输入：10.2.3.120合法
输入：10.2.3.11111 不合法
'''
class Solution:
    def judgeIP(self,str):
        if str.count('.') != 3:
            return False
        for item in str.split('.'):
            if int(item) > 255 or int(item) < 0:
                return False
        return True

if __name__ == '__main__':
    str1 = '098.00000.0'
    str2 = '10.9.9.8'
    str3 = '10.0.1890.111'
    str4 = '098.10.68.94'

    s = Solution()
    print s.judgeIP(str1)
    print s.judgeIP(str2)
    print s.judgeIP(str3)
    print s.judgeIP(str4)