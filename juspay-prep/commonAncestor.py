
from typing import Optional, List
from collections import deque

class Node:
    def __init__(self, val = 0, left = None, right = None ) -> None:
        self.val = val 
        self.right = right 
        self.left = left 
        pass

def builder(nums : List ) -> Optional[Node]:
    if not nums or nums[0] == -1:
        return 
    root = Node(nums[0])
    quq = deque([root])
    i = 1
    while quq and i < len(nums):
        node = quq.popleft()
        if i < len(nums) and nums[i] != -1:
            node.left = Node(nums[i])
            quq.append(node.left)
        i += 1 
        if i < len(nums) and nums[i] != -1:
            node.right = Node(nums[i])
            quq.append(node.right)
        i += 1 

    return root 

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

def commonAncestor(tree, p, q):
    if not tree:
        return None 
    if tree.val == p or tree.val == q:
        return tree 
    left = commonAncestor(tree.left, p, q)
    right = commonAncestor(tree.right, p, q)

    if left and right:
        return tree 
    return left if left else right

def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    tree = builder(arr)
    inorder(tree)
    result = commonAncestor(tree, 2, 5)
    return result 
