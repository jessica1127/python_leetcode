#/usr/lib/python
#coding:utf-8
'''
如果我们已知二叉树的前序遍历和中8序遍历，求这棵二叉树的后序遍历
'''

pre_list = list('12473568')
mid_list = list('47215386')

afterList = []

def findTree(preList, midList, afterList):
    print "preList=",preList
    print "midList=",midList
    if len(preList) == 0:
        return
    if len(preList) == 1:
        afterList.append(preList[0])
        return
    root = preList[0]
    print "root=",root
    n = midList.index(root)
    print "n=",n
    findTree(preList[1:n+1], midList[:n], afterList)
    findTree(preList[n+1:], midList[n+1:], afterList)
    afterList.append(root)
    print "afterList====",afterList
    return afterList


if __name__=='__main__':
    pre_list = list('12473568')
    mid_list = list('47215386')

    afterList = []
    print findTree(pre_list, mid_list, afterList)
