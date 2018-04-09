#!/usr/lib/python env
#coding=utf-8
#给定一个字符串，求出这个字符串中各个字符出现的次数

class Solution:
    def findStrEach(self, str1):
        result = []
        for each in str1:
            num = str1.count(each)
            num_str = each + ":" + str(num)
            if num_str not in result:
                result.append(num_str)
        print "original str1={0}".format(str1)
        for item in result:
            print item

    def findFirstTargetString(self, str1, target):
        len_str = len(str1)
        len_t = len(target)
        for i in range(0, len_str-len_t+1):
            print "str1[i:(i+len_t)]==",str1[i:(i+len_t)]
            if str1[i:(i+len_t)] == target:
                print "find your target at : ", i
                return i
            else:
                i += 1




if __name__ == '__main__':
    str1= 'aabbbb8jdlddddppionn'
    s = Solution()
    s.findStrEach(str1)

    s.findFirstTargetString(str1, "dddd")