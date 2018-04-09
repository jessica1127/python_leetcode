class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preSearch(root):
    if root == None:
        return
    print root.value
    preSearch(root.left)
    preSearch(root.right)

def midSearch(root):
    if root == None:
        return
    midSearch(root.left)
    print root.value
    midSearch(root.right)



if __name__ == '__main__':
    tree = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G', left=Node('H'))))
    preSearch(tree)
    print "Below is mid search: "
    midSearch(tree)