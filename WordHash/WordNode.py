class WordNode:
    def __init__(self, key, value):
        self.word = key
        self.count = value
        self.next = None

    def increment(self):
        self.count += 1
