from collections import OrderedDict


class Node:
    def __init__(self, name, data=None):
        self._name = name
        self._outgoing_edges = OrderedDict()
        self._incoming_edges = OrderedDict()
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)

    def add_outgoing_edge(self, edge):
        self._outgoing_edges[edge.destination()] = edge

    def add_incoming_edge(self, edge):
        self._incoming_edges[edge.source()] = edge

    def remove_outgoing_edge(self, edge):
        del self._outgoing_edges[edge.destination()]

    def remove_incoming_edge(self, edge):
        del self._incoming_edges[edge.source()]

    def name(self):
        return self._name

    def outgoing_edges(self):
        return list(self._outgoing_edges.values())

    def incoming_edges(self):
        return list(self._incoming_edges.values())

    def edge_to(self, node):
        return self._outgoing_edges.get(node)

    def edge_from(self, node):
        return self._incoming_edges.get(node)

    def clear(self):
        for key, value in vars(self).items():
            if not key.startswith("_"):
                delattr(self, key)

    def __str__(self):
        res = self._name + "\n"
        for key, value in vars(self).items():
            if not key.startswith("_"):
                res += "    " + str(key) + " : " + str(value) + "\n"

        return res





