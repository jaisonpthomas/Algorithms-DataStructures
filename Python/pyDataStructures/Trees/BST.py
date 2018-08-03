"""
Implementation based on tutorial from joeyJames
https://github.com/joeyajames/Python/blob/master/Trees/bst.py

Personal Modifications:
-significantly simplified node removal code
-added levelOrder Traversal
"""

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False

        elif data < self.value:
            if self.left:
                self.left.insert(data)
            else:
                self.left = TreeNode(data)
                return True

        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = TreeNode(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif data < self.value:
            if self.left:
                self.left.find(data)
            else:
                return False
        else:
            if self.right:
                self.right.find(data)
            else:
                return False

    def getHeight(self):
        if self.left and self.right:
            return 1 + max(self.left.getHeight(), self.right.getHeight())
        elif self.left:
            return 1 + self.left.getHeight()
        elif self.right:
            return 1 + self.right.getHeight()
        else:
            return 1

    def preOrder(self):
        print(str(self.value), end = " ")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(str(self.value), end = " ")

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(str(self.value), end = " ")
        if self.right:
            self.right.inOrder()

    def numNodes(self):
        numNodes = 1
        if self.left:
            numNodes += self.left.numNodes()
        if self.right:
            numNodes += self.right.numNodes()
        return numNodes

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = TreeNode(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return -1

    def preOrder(self):
        if self.root is not None:
            print("PreOrder: ")
            self.root.preOrder()

    def postOrder(self):
        if self.root is not None:
            print("PostOrder: ")
            self.root.postOrder()

    def inOrder(self):
        if self.root is not None:
            print("In Order: ")
            self.root.inOrder()
            
    def levelOrder(self):
        if self.root:
            print("Level Order Traversal")
            levelQueue = [self.root]
            while len(levelQueue):
                nextLevelQueue = []
                for node in levelQueue:
                    print(node.value, end = " ")
                    if node.left:
                        nextLevelQueue.append(node.left)
                    if node.right:
                        nextLevelQueue.append(node.right)
                levelQueue = nextLevelQueue
                print()
        else:
            return False
                

    def numNodes(self):
        if self.root:
            return self.root.numNodes()
        else:
            return 0

    def remove(self, data):
        if self.root is None:
            return False
            
        elif self.root.value == data:
            rootFlag = True

        parent = None
        node = self.root
        
        # find node to remove (will be skipped if rootFlag is True)
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.left
            elif data > node.value:
                node = node.right
        
        # case 1: data not found
        if node is None or node.value != data:
            return False
            
        # case 2: remove-node has no children
        elif node.left is None and node.right is None:
            if rootFlag:
                self.root = None
            elif data < parent.value:
                parent.left = None
            else:
                parent.right = None
            return True
            
        # case 3: remove-node has left child only
        elif node.left and node.right is None:
            if rootFlag:
                self.root = self.root.left
            elif data < parent.value:
                parent.left = node.left
            else:
                parent.right = node.left
            return True
            
        # case 4: remove-node has right child only
        elif node.left is None and node.right:
            if rootFlag:
                self.root = self.root.right
            elif data < parent.value:
                parent.left = node.right
            else:
                parent.right = node.right
            return True
            
        # case 5: remove-node has left and right children
        else:
            delNodeParent = node
            delNode = node.right
            while delNode.left:
                delNodeParent = delNode
                delNode = delNode.left
            
            node.value = delNode.value
            if delNode.right:
                if delNodeParent.value > delNode.value:
                    delNodeParent.left = delNode.right
                elif delNodeParent.value < delNode.value:
                    delNodeParent.right = delNode.right
            else:
                if delNode.value < delNodeParent.value:
                    delNodeParent.left = None
                else:
                    delNodeParent.right = None
            return True
        
if __name__ == "__main__":
    bst = Tree()
    bstNodes = [12,  5,15,  3,9,13,22,  1,8,11,16,  17]
    for num in bstNodes:
        bst.insert(num)
    bst.levelOrder()
    print('Height = ', bst.getHeight())
    print('Size = ', bst.numNodes())
    print(bst.remove(12))
    bst.levelOrder()