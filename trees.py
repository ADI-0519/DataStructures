from collections import deque
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    



A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F


# Pre-order traversal (DFS) Time: O(n) Space:O(n) Goes node, then left, then right.

def pre_order(node):
    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)

# Pre-order traversal (DFS) Time: O(n) Space:O(n) Goes left subtree, then prints node, then right.

def in_order(node):
    if not node:
        return

    in_order(node.left)
    print(node)
    in_order(node.right)


#in_order(A)

#Post-order traversal (DFS) Time: O(n) Space:O(n) Goes left, then right, then prints node.


def post_order(node):
    if not node:
        return

    post_order(node.left)
    post_order(node.right)
    print(node)

#post_order(A)

# Pre-order traversal using iteration

def pre_order_iterative(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)



pre_order_iterative(A)

# BFS - level order traversal

def BFS(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        q.append(node.left)
        q.append(node.right)
