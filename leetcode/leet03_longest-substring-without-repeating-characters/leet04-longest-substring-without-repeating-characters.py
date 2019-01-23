#-*-coding:utf-8
#!/usr/lib/python

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        '''
        思路：遍历字符串中的每一个元素，借助一个辅助键值对来存储某个元素最后一次出现的下表，用一个整形变量存储当前无重复字符串的开始下标
        时间复杂度O(n)O(n)，空间复杂度O(n)O(n)。
        '''
        res = 0
        start = 0
        d = {}
        for i in range(len(s)):
            print "s[i]= ",s[i]," d= ",d, " i= ",i
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1
            tmp = i - start + 1
            d[s[i]] = i
            res = max(res, tmp)
        return res

if __name__ == '__main__':
    s = "abcabccccc"
    so = Solution()
    print so.lengthOfLongestSubstring(s)