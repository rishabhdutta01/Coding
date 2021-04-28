class Edge:

    def __init__(self, node1, node2, data = None):
        self._node1 = node1
        self._node2 = node2
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)

    def nodes(self):
        return [self._node1, self._node2]

    def source(self):
        return self._node1

    def destination(self):
        return self._node2

    def is_directed(self):
        return True;

    def clear(self):
        for key, value in vars(self).items():
            if not key.startswith("_"):
                delattr(self, key)

    def __str__(self):
        res = self._node1.name() + " --> " + self._node2.name() + "\n"
        for key, value in vars(self).items():
            if not key.startswith("_"):
                res += "    " + str(key) + " : " + str(value) + "\n"

        return res
