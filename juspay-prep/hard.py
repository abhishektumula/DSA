from collections import deque 
from typing import List, Optional , Union

class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 
        pass 

def builder(nums : List[int] ) -> Optional[TreeNode]:

    if not nums or nums[0] == -1:
        return None 

    root = TreeNode(nums[0])
    quq = deque([root])
    i = 1

    while quq and i < len(nums):
        node = quq.popleft()
        if i < len(nums) and nums[i] != -1:
            node.left = TreeNode(nums[i])
            quq.append(node.left)
        i+= 1

        if i < len(nums) and nums[i] != -1:
            node.right = TreeNode(nums[i])
            quq.append(node.right)
        i+= 1

    return root 

def display(node :Optional[TreeNode] ):
    if node:
        display(node.left)
        print(node.val)
        display(node.right)

def levelOrder(head) -> List:
    if not head:
        return [] 
   
    result = []
    quq = deque([head])
    while quq:
        lenght = len(quq)
        inner = []

        for _ in range(lenght):
            node = quq.popleft()
            inner.append(node.val)

            if node.left:
                quq.append(node.left)

            if node.right:
                quq.append(node.right)

        result.append(inner)

    return result

def isSymetry(left, right):
    if not left and not right:
        return True 
    if not left or not right:
        return False 
    return isSymetry(left.left,right.right) and isSymetry(left.right, right.left)

def solution():
    N = int(input())
    arr = list(map(int, input().split()))[:N]
    if not builder(arr):
        return -1 
    else:
        tree = builder(arr)
    display(tree)
    fHalf, sHalf = tree.left, tree.right
    print(isSymetry(fHalf, sHalf))
    print(levelOrder(tree))

print(solution())

