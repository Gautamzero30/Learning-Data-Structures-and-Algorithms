class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree
        self.keys = []  # Keys in node
        self.children = []  # Children references
        self.leaf = leaf

    def insert_non_full(self, k):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(None)
            while i >= 0 and k < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = k
        else:
            while i >= 0 and k < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == (2 * self.t - 1):
                self.split_child(i, self.children[i])
                if k > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(k)

    def split_child(self, i, y):
        z = BTreeNode(y.t, y.leaf)
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys[self.t - 1])

        z.keys = y.keys[self.t:(2 * self.t - 1)]
        y.keys = y.keys[0:(self.t - 1)]

        if not y.leaf:
            z.children = y.children[self.t:(2 * self.t)]
            y.children = y.children[0:self.t]

    def traverse(self):
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=" ")
        if not self.leaf:
            self.children[len(self.keys)].traverse()


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def traverse(self):
        if self.root:
            self.root.traverse()
        print()

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            s = BTreeNode(self.t, False)
            s.children.insert(0, root)
            s.split_child(0, root)
            i = 0
            if s.keys[0] < k:
                i += 1
            s.children[i].insert_non_full(k)
            self.root = s
        else:
            root.insert_non_full(k)


# Example usage
if __name__ == "__main__":
    btree = BTree(3)
    for num in [1, 3, 7, 10, 11, 13, 14, 15, 18, 16, 19, 24, 25]:
        btree.insert(num)

    print("B-Tree traversal:")
    btree.traverse()
