import sys

from Node import Node, NullNode


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)

        # Base case
        if self.root is None:
            node.red = False
            self.root = node
            return

        curr = self.root
        parent = curr
        while type(curr) != NullNode:
            parent = curr
            if node.value < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        # Assign parents and siblings
        node.parent = parent
        if node.value < node.parent.value:
            node.parent.left = node
        else:
            node.parent.right = node

        self.fix_insert(node)

    def fix_insert(self, node):
        while node.parent.red and node != self.root:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.red:
                    node.parent.red = False
                    uncle.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.red:
                    node.parent.red = False
                    uncle.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.left_rotate(node.parent.parent)
        self.root.red = False

    def left_rotate(self, node):
        insertedNode = node.right
        node.right = insertedNode.left
        if type(insertedNode.left) != NullNode:
            insertedNode.left.parent = node

        insertedNode.parent = node.parent
        if type(node.parent) == NullNode:
            self.root = insertedNode
        else:
            if node == node.parent.left:
                node.parent.left = insertedNode
            else:
                node.parent.right = insertedNode
        insertedNode.left = node
        node.parent = insertedNode

    def right_rotate(self, node):
        insertedNode = node.left
        node.left = insertedNode.right
        if type(insertedNode.right) != NullNode:
            insertedNode.right.parent = node

        insertedNode.parent = node.parent
        if type(node.parent) == NullNode:
            self.root = insertedNode
        else:
            if node == node.parent.right:
                node.parent.right = insertedNode
            else:
                node.parent.left = insertedNode
        insertedNode.right = node
        node.parent = insertedNode

    def get_root(self):
        return self.root

    def printTree(self, node, level=0):
        if type(node) != NullNode:
            self.printTree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value, "R" if node.red else "B")
            self.printTree(node.left, level + 1)

    def search(self, key):
        curr = self.root
        while type(curr) != NullNode:
            if key == curr.value:
                return curr
            elif key < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def minimum(self):
        return self.minimum_from_node(self.root)

    def minimum_from_node(self, node):
        if type(node) == NullNode:
            return None

        while type(node.left) != NullNode:
            node = node.left
        return node.value

    def maximum(self):
        return self.maximum_from_node(self.root)

    def maximum_from_node(self, node):
        if type(node) == NullNode:
            return None

        while type(node.right) != NullNode:
            node = node.right
        return node.value

    def successor(self, node):
        if type(node) == NullNode:
            return None

        if type(node.right) != NullNode:
            return self.minimum_from_node(node.right)

        parent = node.parent
        while type(parent) != NullNode and node == parent.right:
            node = parent
            parent = parent.parent
        return parent.value

    def predecessor(self, node):
        if type(node) == NullNode:
            return None

        if type(node.left) != NullNode:
            return self.maximum_from_node(node.left)

        parent = node.parent
        while type(parent) != NullNode and node == parent.left:
            node = parent
            parent = parent.parent
        return parent.value

    def sort(self):
        return self.inorder()

    def inorder(self):
        return self.inorder_from_node(self.root)

    def inorder_from_node(self, node):
        if type(node) != NullNode:
            self.inorder_from_node(node.left)
            sys.stdout.write(repr(node.value) + " ")
            self.inorder_from_node(node.right)

    def height(self):
        return self.height_from_node(self.root)

    def height_from_node(self, node):
        if node is None or type(node) == NullNode:
            return 0
        else:
            lheight = self.height_from_node(node.left)
            rheight = self.height_from_node(node.right)

            if (lheight > rheight):
                return lheight + 1
            else:
                return rheight + 1
