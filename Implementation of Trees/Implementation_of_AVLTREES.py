class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.height = 1

def getHeight(root):
    if not root:
        return 0
    return root.height

def getBalance(root):
    if not root:
        return 0
    return getHeight(root.left) - getHeight(root.right)

def rightRotate(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    return y

def leftRotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    return y

def insert(root, key):
    if not root:
        return Node(key)
    elif key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalance(root)

    # Left Left
    if balance > 1 and key < root.left.value:
        return rightRotate(root)

    # Right Right
    if balance < -1 and key > root.right.value:
        return leftRotate(root)

    # Left Right
    if balance > 1 and key > root.left.value:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # Right Left
    if balance < -1 and key < root.right.value:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def inorder(root, res):
    if not root:
        return
    inorder(root.left, res)
    res.append(root.value)
    inorder(root.right, res)

if __name__ == "__main__":
    data = [3,2,1,4,5,6]
    root = None
    for key in data:
        root = insert(root, key)

    k = []
    inorder(root, k)
    print(f"The required AVL tree in inorder is:\n{k}")
