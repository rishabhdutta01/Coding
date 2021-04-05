class NullNode:
    def __init__(self):
        self.value = None
        self.red = False
        self.parent = None
        self.left = None
        self.right = None


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = NullNode()
        self.left = NullNode()
        self.right = NullNode()
        self.red = True
