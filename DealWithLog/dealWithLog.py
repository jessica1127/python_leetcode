#coding=utf-8
'''
编程题：log分析。 给你一份10w行的log文件，内容如下
20180118 100031 hello world
20180118 100032 Exception:Null Pointer
20180118 100101 something normal
20180118 100215 Exception: invalid parameter
请按小时打印出exception的种类和数量，如：
20180118 10 Exception:Null Pointer 6
20180118 10 Exception:invalid parameter 15
20180118 11 ....

'''