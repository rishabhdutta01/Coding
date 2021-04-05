class Node:
    """This class represents a node in a linked list."""

    def __init__(self, value=None):
        """
        Constructor
        :param value: value contained in the node
        """
        self.value = value
        self.next = None


class LinkedList:
    """This class represents a linked list."""

    def __init__(self):
        """Constructor"""
        self.header = None

    def add_element(self, value):
        """
        Add a node with specified value in the linked list.
        :param value: value contained in the node
        """
        if self.header is None:
            self.header = Node(value)
        else:
            current = self.header
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def shortened_list(self, position):
        """
        Shorten a list by a specified number from the beginning.
        :param position: Number of nodes to be deleted
        :return: New header in the list
        """
        if self.header is None:
            return None

        current = self.header
        while position != 0:
            position -= 1
            current = current.next
        return current

    def add_list(self, altlist, position=0):
        """
        Append a new list.
        :param altlist: List to be appended
        :param position: First node to be appended
        """
        if self.header is None:
            self.header = altlist.shortened_list(position)
        else:
            current = self.header
            while current.next is not None:
                current = current.next
            current.next = altlist.shortened_list(position)

    def print_list(self):
        """Print the list."""
        current = self.header
        while current is not None:
            print("->", current.value)
            current = current.next

    def length(self):
        """
        Return length of the list.
        :return: Length of the list
        """
        count = 0
        current = self.header
        while current is not None:
            current = current.next
            count += 1
        return count

    def find_intersection(self, altlist):
        """
        If the lists intersect then the first intersection value is returned else -1 is returned.
        :param altlist: List to compare to for intersection
        :return: Intersecting node value
        """
        if self.header is None or altlist.header is None:
            return None

        len1 = self.length()
        len2 = altlist.length()

        current1 = self.header
        current2 = altlist.header
        if len1 > len2:
            current1 = self.shortened_list(len1 - len2)
        else:
            current2 = altlist.shortened_list(len2 - len1)

        while current1 is not current2:
            current1 = None if current1.next is None else current1.next
            current2 = None if current2.next is None else current2.next

        if current1 is not None:
            return current1.value
        else:
            return -1
