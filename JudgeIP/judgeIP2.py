#coding:utf-8
#/usr/lib/python
import re

def judgeIPRegular(str_given):
    regular_express = '^(25[0-5]|2[0-4]\\d|1\\d{2}|[1-9]\\d|[1-9])\\.' + '(25[0-5]|2[0-4]\\d|1\\d{2}|[1-9]\\d|\\d)\\.' + '(25[0-5]|2[0-4]\\d|1\\d{2}|[1-9]\\d|\\d)\\.' + '(25[0-5]|2[0-4]\\d|1\\d{2}|[1-9]\\d|\\d)$'
    compile_ip = re.compile(regular_express)
    if compile_ip.match(str_given):
        print "str_give={}, True".format(str_given)
        return True
    else:
        print "str_give={}, False".format(str_given)
        return False



if __name__ == '__main__':
    str0 = '0.0.1'
    str1 = '0.23.67.78'
    str2 = '127.35.63.85'
    str3 = '194.0.0.0'
    str4 = '198.255.255.255'
    str5 = '156.35.23.255'
    str6 = '180.53.32.255'
    str7 = '200.0.0.0'
    str8 = '160.0.0.0'
    str9 = '210.255.255'


    judgeIPRegular(str0)
    judgeIPRegular(str1)
    judgeIPRegular(str2)
    judgeIPRegular(str3)
    judgeIPRegular(str4)
    judgeIPRegular(str5)


