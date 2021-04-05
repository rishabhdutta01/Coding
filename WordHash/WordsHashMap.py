from WordsLinkedList import WordsLinkedList


class WordsHashMap:
    def __init__(self, size):
        self.size = size
        self.array = [WordsLinkedList() for _ in range(self.size)]

    def custom_hash(self, key):
        prime = 31
        # p =53
        hash_value = 0
        prime_pow = 1

        for c in key:
            hash_value = (hash_value + (ord(c) - ord('a') + 1) * prime_pow) % self.size
            prime_pow = (prime_pow * prime) % self.size

        return hash_value

    def insert(self, key, value):
        h = self.custom_hash(key)
        self.array[h].insert(key, value)

    def increase(self, key):
        h = self.custom_hash(key)
        self.array[h].increase(key)

    def find(self, key):
        h = self.custom_hash(key)
        value = self.array[h].find(key)
        if value is not None:
            return value
        else:
            return -1

    def delete(self, key):
        h = self.custom_hash(key)
        self.array[h].delete(key)

    def list_all_keys(self):
        elements = []
        for ll in self.array:
            elements += ll.list_all_keys()
        return '\n'.join(elements)

    def print_hash(self):
        elements = []
        for ll in self.array:
            elements.append(ll.print_elements())
        return '\n'.join(elements)
