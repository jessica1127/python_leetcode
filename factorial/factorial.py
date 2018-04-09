#!/usr/bin/python env
#coding=utf-8
# 英文factorial意思是阶乘，6的阶乘6！=6*5*4*3*2*1， 1！=1， 0！=1

class Solution:
    def factorial(self, num):
        factorial = 1
        if num == 0:
            return 1
        elif num < 0:
            print "num has no factorial!"
        else:
            for i in range(1, num+1):
                factorial = i * factorial
            return factorial

## n个数以内阶乘的和

    def factorial_sum(self, num):
        sum = 0
        for num_iter in range(0, num+1):
            sum += self.factorial(num_iter)
        print "total sum =", sum




if __name__ == '__main__':
    num = 3
    num2 = 10
    s = Solution()
    fac = s.factorial(num)
    fac2= s.factorial(num2)

    print "{0}!={1}".format(num, fac)
    print "{0}!={1}".format(num2, fac2)

    s.factorial_sum(num)