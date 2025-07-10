import random
class BinaryTree:
    
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def Insertion(self, value : int):
        if not self.data:
            print(f"(init new tree) : {self.data}")
            self.data = BinaryTree(value)
            return 
        elif self.data == value:
            print(f"(duplicate) : {value}")
            return 
        else:
            if self.data < value :
                if self.right:
                    self.right.Insertion(value)
                else:
                    self.right = BinaryTree(value)
                    print(f"(right : {self.data}) :: {value}")
                    return
            else:
                if self.left:
                    self.left.Insertion(value)
                else:
                    self.left = BinaryTree(value)
                    print(f"(left : {self.data}) :: {value}")
                    return
                
    def findMin (self, root):
        while root.left :
            root = root.left

        return root
    
    def findMax (self, root):
        while root.right:
            root = root.right
        
        return root

    def deletion(self, target : int):
        if not self:
            print(f"(null node)")
        if target < self.data:
            if self.left:
                self.left = self.left.deletion(target)
        elif target > self.data:
            if self.right:
                self.right = self.right.deletion(target)

        else:
            # case 1: if node is child node :
            if not self.left and not self.right:
                print(f"(found at leaf node) :: ")
                return None 
            #  case 2 : if node has 1 children
            if not self.left:
                print(f"(found with 1 children) :: ")
                return self.right 
            if not self.right:
                print(f"(found with 1 children) :: ")
                return self.left
            # case 3 : if node has 2 children
            else:
                # step 1: find the largest element in the right side ..
                # step 2: interchange pos of  the largest (last node) with the target node(now
                # target node goes to the end)
                # now target is the leaf Node.. which executes case 1
                print(f"(found with 2 children) :: ")
                minimumValue = self.right.findMin(self.right)
                self.data = minimumValue.data
                self.right = self.right.deletion(minimumValue.data) 

    def searchOperation (self, target : int):
        if not self:
            print(f"(null node)")
            return 
        if self.data == target:
            return f"(found)"
        elif self.data > target:
            return self.left.searchOperation(target)
        else:
            return self.right.searchOperation(target)  

def inOrderTraversal (node):
    if node:
        inOrderTraversal(node.left)
        print(f"{node.data}")
        inOrderTraversal(node.right)

def preOrderTraversal (node):
    if node:
        print(f"{node.data}")
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)
    
ele = [random.randint(1,10) for _ in range(10)]
print(f"elements :{ele}")
for each in range(len(ele)):
    if each == 0:
        btree = BinaryTree(ele[each])
        print(f"{ele[each]} is the root element.")
    else:
        btree.Insertion(ele[each])
        print(f"(added): {ele[each]}")

print(f"inOrder Traversal :: {inOrderTraversal(btree)}")
print(f"preOrder Traversal :: {preOrderTraversal(btree)}")
btree.deletion(random.randint(1, 10))
print(f"inOrder Traversal :: {inOrderTraversal(btree)}")
print(f"preOrder Traversal :: {preOrderTraversal(btree)}")
 