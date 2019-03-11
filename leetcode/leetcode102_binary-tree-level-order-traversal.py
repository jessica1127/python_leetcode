'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

'''
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#         
class Solution():
    def levelOrder1(self, root):
        queue = []
        output = []
        level = []

        if root:
            queue.append(root)
            queue.append(None)

        while queue:
            node = queue.pop(0)   # first element in queue
            if node:
                print "node.val = ", node.val
                level.append(node.val)
                if node.left:
                    print "node.left = ", node.left
                    queue.append(node.left)
                if node.right:
                    print "node.left = ", node.left
                    queue.append(node.right)
                print "level = ", level
            else:
                output.append(level)
                if queue:
                    queue.append(None)
                print "000 output = ", output
                level= []
        print "output = ", output
        return output

    def levelOrder(self, root):
        #use deque
        result = []
        level = []
        if not root:
            return []
        q = deque()
        q.append(root)
        q.append(None)
        while True:
            node = q[0]
            q.popleft()
            if not node:
                result.append(level)
                if len(q) == 0:
                    break
                else:
                    q.append(None)
                    level = []
            else:
                level.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        print "result = ", result
        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root_left = TreeNode(9)
    root_right = TreeNode(20)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left  = TreeNode(15)
    root.right.right = TreeNode(7)
    
    s.levelOrder(root)