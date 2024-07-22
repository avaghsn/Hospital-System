class BSTNode:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return not self.root

    def insert(self, data, key):
        if self.is_empty():
            self.root = BSTNode(data, key)
        else:
            self.insert_(self.root, data, key)

    def insert_(self, root, data, key):
        if key > root.key:
            if not root.right:
                root.right = BSTNode(data, key)
            else:
                self.insert_(root.right, data, key)
        elif key < root.key:
            if not root.left:
                root.left = BSTNode(data, key)
            else:
                self.insert_(root.left, data, key)
        else:  # if key already exits
            root.data = data

    def delete(self, key):
        self.root = self.delete_(self.root, key)

    def delete_(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self.delete_(node.left, key)
        elif key > node.key:
            node.right = self.delete_(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                node.key, node.value = self.find_min_(node.right)
                node.right = self.delete_(node.right, node.key)
        return node

    def find_min(self):
        if not self.root:
            return None
        return self.find_min_(self.root)

    def find_min_(self, node):
        while node.left:
            node = node.left
        return node.key, node.data

    def find(self, key):
        return self.find_(self.root, key)

    def find_(self, node, key):
        if not node:
            return None
        if key < node.key:
            return self.find_(node.left, key)
        elif key > node.key:
            return self.find_(node.right, key)
        else:
            return node.data

