#coding:utf-8
#/usr/lib/python

'''
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

'''
python自带函数做法：
'''

class Solution:
    def replaceSpace(self, s):
        return s.replace(" ", '%20')

    def replaceNotUsePythonMethod(self, s):
        result = ""
        for ss in s:
            if ss == ' ':
                result += '%20'
            else:
                result += ss
        return result



if __name__ == "__main__":
    str1 = "Hello Word !"
    solution = Solution()
    print "Mothod1=",solution.replaceSpace(str1)

    print "Mothod2=", solution.replaceNotUsePythonMethod(str1)
