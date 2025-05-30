#NOTE: This files contains the implementation of the trees data structure....
import time
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None 

    def insertiontoBST(self, value):
        if not self.data :
            self.data = BinaryTree(value)
        if self.data == value: 
            return
        if self.data < value:
            if self.right:
                self.right.insertiontoBST(value)
            else:
                self.right = BinaryTree(value)
        else:
            if self.left:
                self.left.insertiontoBST(value)
            else:
                self.left = BinaryTree(value)


root = BinaryTree(10)
root.insertiontoBST(1)
root.insertiontoBST(2)
root.insertiontoBST(5)  
root.insertiontoBST(3)  
root.insertiontoBST(7)  
root.insertiontoBST(12) 

def inorderTraversal(node):
    if node:
        inorderTraversal(node.left)
        print(f"{node.data}", end = "-->", flush = True)
        time.sleep(0.4)
        inorderTraversal(node.right)

inorderTraversal(root)


