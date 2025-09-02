class BTreeNode:
    def __init__(self, t, leaf=False):
        """
        t: Minimum degree of B-Tree
        leaf: Boolean indicating whether node is a leaf
        """
        self.t = t
        self.leaf = leaf
        self.keys = []       # list of keys
        self.children = []   # list of children

    def traverse(self):
        """Prints all keys in this subtree in sorted order"""
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=" ")
        if not self.leaf:
            self.children[len(self.keys)].traverse()

    def search(self, k):
        """Search for key k in subtree rooted with this node"""
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1
        if i < len(self.keys) and self.keys[i] == k:
            return self
        if self.leaf:
            return None
        return self.children[i].search(k)


class BTree:
    def __init__(self, t):
        self.root = None
        self.t = t  # Minimum degree

    def traverse(self):
        if self.root:
            self.root.traverse()
        else:
            print("Tree is empty")

    def search(self, k):
        return None if self.root is None else self.root.search(k)

    def insert(self, k):
        if self.root is None:
            self.root = BTreeNode(self.t, True)
            self.root.keys.append(k)
        else:
            if len(self.root.keys) == 2 * self.t - 1:
                # Root is full, split it
                new_root = BTreeNode(self.t, False)
                new_root.children.append(self.root)
                self._split_child(new_root, 0)
                i = 0
                if new_root.keys[0] < k:
                    i += 1
                self._insert_non_full(new_root.children[i], k)
                self.root = new_root
            else:
                self._insert_non_full(self.root, k)

    def _insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)  # Temporary placeholder
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self._split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    def _split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(t, y.leaf)

        parent.keys.insert(i, y.keys[t - 1])
        parent.children.insert(i + 1, z)

        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]

        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]


# Example usage
if __name__ == "__main__":
    btree = BTree(3)  # B-Tree with minimum degree 3
    nums = [10, 20, 5, 6, 12, 30, 7, 17]

    for num in nums:
        btree.insert(num)

    print("Traversal of B-tree:")
    btree.traverse()

    k = 6
    print(f"\n\nSearching for {k}:",
          "Found" if btree.search(k) else "Not Found")
