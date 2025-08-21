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

def in_order_iterative(root):
    stk = [root]
    curr = node

    while stk or curr:
        while curr:
            stk.append(curr)
            curr = curr.left

        curr = stk.pop()
        print(curr)
        curr = curr.right   



# BFS - level order traversal

def BFS(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        q.append(node.left)
        q.append(node.right)


# Building a tree from a list
def build_tree_from_list(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while i < len(lst):
        current = queue.popleft()
        if i < len(lst) and lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root

def build_tree(root,val):
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = build_tree(root.left, val)
    else:
        root.right = build_tree(root.right, val)

    return root

