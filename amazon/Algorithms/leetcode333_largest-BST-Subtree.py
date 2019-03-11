import math
'''
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.

'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#ret:  N, n, min, max
#N: stands for the size of the largest BST in the tree
#If the tree is a BST, then n is the number of nodes, otherwise it's -infinity
#If the tree is a BST, then min and max are the minimum/maxmum value in the tree 
class Soltion(object):
    def largestBSTSubtree(self, root):
        print "111root==",root
        def dfs(root):
            print "000root==",root
            if not root:
                return 0, 0, float('inf'), float('-inf')  #min is inf, max is -inf
            N1, n1, min1, max1 = dfs(root.left)
            N2, n2, min2, max2 = dfs(root.right)
            n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf') #n is the number of nodes, otherwise it is -infinity
            return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)
        return dfs(root)[0]

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode('null')  #pay attention, this node should not be string = "null"
    root.right.right = TreeNode(7)
    s = Soltion()
    N = s.largestBSTSubtree(root)
    print "N=", N
















