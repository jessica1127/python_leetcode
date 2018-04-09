'''
http://www.jiuzhang.com/solutions/first-bad-version/#tag-highlight-lang-python
代码库的版本号是从 1 到 n 的整数。某一天，有人提交了错误版本的代码，因此造成自身及之后版本的代码在单元测试中均出错。请找出第一个错误的版本号。

你可以通过 isBadVersion 的接口来判断版本号 version 是否在单元测试中出错，具体接口详情和调用方法请见代码的注释部分。
'''

class Solution:
    '''
    @param n: An integer
    @returns: An integer which is the first bad version
    '''
    def findFirstBadVersion(self, n):
        start, end = 1, n
        while start + 1 < end:
            mid = start + (start - end)//2
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid
        if SVNRepo.isBadVersion(start):
            return start

        return end




