from collections import deque

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def build_tree(elements):
    root = None
    for el in elements:
        root = insert(root, el)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def dfs(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.value, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def search(root, key):
    if root is None or root.value == key:
        return root
    if key < root.value:
        return search(root.left, key)
    return search(root.right, key)

elements = [20, 10, 30, 5, 15, 25, 35]
root = build_tree(elements)

print("InOrder:", end=" "); inorder(root); print()
print("PostOrder:", end=" "); postorder(root); print()
print("PreOrder:", end=" "); preorder(root); print()
print("BFS:", end=" "); bfs(root); print()
print("DFS:", end=" "); dfs(root); print()

key = 25
found = search(root, key)
print(f"\nSearch {key}:", "Found" if found else "Not Found")

              
              