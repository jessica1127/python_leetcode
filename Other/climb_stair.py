#coding=utf-8
#!/usr/bin/python
'''
方法1:递归

设青蛙跳上n级台阶有f(n)种方法，把这n种方法分为两大类，第一种最后一次跳了一级台阶，这类方法共有f(n-1)种，第二种最后一次跳了两级台阶，这种方法共有f(n-2)种，则得出递推公式f(n)=f(n-1)+f(n-2),显然，f(1)=1,f(2)=2，递推公式如此
'''

class Solution:
    def clim_stair(self, n):
        if n == 1 or n == 2:
            return n
        else:
            return self.clim_stair(n-1)+self.clim_stair(n-2)


if __name__ == '__main__':
    n = 5
    Solution().clim_stair(5)