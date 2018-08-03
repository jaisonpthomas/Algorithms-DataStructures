class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        
    def numNodes(self):
        if self is not None:
            numNodes = 1
            if self.left:
                numNodes += self.left.numNodes()
            if self.right:
                numNodes += self.right.numNodes()
            return numNodes
        else:
            return 0
        
root = TreeNode(6)
l21 = TreeNode(3)
l22 = TreeNode(8)
l31 = TreeNode(2)
l32 = TreeNode(4)
l33 = TreeNode(7)
l34 = TreeNode(9)
l41 = TreeNode(1)

root.left = l21
root.right = l22

l21.left = l31
l21.right = l32

l22.left = l33
l22.right = l34

l31.left = l41
print(root.numNodes())


#        6
#    3       8
#  2   4   7    9