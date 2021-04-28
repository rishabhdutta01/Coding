class Path:
    def __init__(self, start):
        self._nodes = [start]
        self._edges = []

    def nodes(self):
        return list(self._nodes)

    def edges(self):
        return list(self._edges)

    def start(self):
        return self._nodes[0]

    def end(self):
        return self._nodes[-1]

    def items(self):
        pos = 0
        for edge in self.edges():
            pos += 1
            yield (edge, self._nodes[pos])

    def append(self, edge, node):
        if not edge.source() == self._nodes[-1] or not edge.destination() == node:
            raise ValueError("Edge is not connecting the new and the previous node")
        self._nodes.append(node)
        self._edges.append(edge)

        return self     # allows function chaining

    def pop(self):
        self._nodes.pop()
        self._edges.pop()

        return self

    def __str__(self):
        res = ""

        for edge in self.edges():
            res += str(edge)

        return res