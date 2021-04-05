from WordNode import WordNode


class WordsLinkedList:
    def __init__(self):
        self.head = WordNode(None, None)

    def search(self, key):
        curr = self.head.next
        while curr:
            if curr.word == key:
                return curr
            curr = curr.next
        return None

    def insert(self, key, value):
        curr = self.search(key)
        if curr:
            curr.increment()
        else:
            node = WordNode(key, value)
            self.head.next, node.next = node, self.head.next

    def increase(self, key):
        curr = self.search(key)
        if curr:
            curr.increment()
        else:
            node = WordNode(key, 1)
            self.head.next, node.next = node, self.head.next

    def find(self, key):
        curr = self.search(key)
        if curr:
            return curr.count
        else:
            return None

    def delete(self, key):
        prev = self.head
        curr = prev.next
        while curr:
            if curr.word == key:
                break
            prev, curr = curr, curr.next
        if curr:
            prev.next = curr.next

    def list_all_keys(self):
        elements = []
        curr = self.head.next
        while curr:
            elements.append(curr.word)
            curr = curr.next

        return elements

    def print_elements(self):
        elements = []
        curr = self.head.next
        while curr:
            elements.append(curr.word + "(" + repr(curr.count) + ")")
            elements.append("->")
            curr = curr.next
        elements.append("null")
        return ''.join(elements)
