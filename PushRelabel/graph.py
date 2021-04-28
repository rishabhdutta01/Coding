from collections import OrderedDict

from Edge import Edge
from Node import Node


class Graph:
    def __init__(self):
        self._nodes = OrderedDict()
        self._edges = []

    def nodes(self):
        return list(self._nodes.values())

    def edges(self):
        return list(self._edges)

    def add_node(self, name, data=None):
        if self.has_node(name):
            raise ValueError("Node %s already exists" % name)
        self._nodes[name] = Node(name, data)
        return self._nodes[name]

    def add_nodes(self, l):
        ret = []
        for name in l:
            ret.append(self.add_node(name))
        return ret

    def add_edge(self, src, dst, data=None):
        srcnode, dstnode = self._node_lookup([src, dst])
        if srcnode is None or dstnode is None:
            raise ValueError("No such node in this graph")
        edge = Edge(srcnode, dstnode, data)
        self._edges.append(edge)
        srcnode.add_outgoing_edge(edge)
        dstnode.add_incoming_edge(edge)
        return edge

    def remove_edge(self, edge):
        if not edge in self._edges:
            return
        self._edges.remove(edge)
        if edge.is_directed():
            edge.source().remove_outgoing_edge(edge)
            edge.destination().remove_incoming_edge(edge)

    def get_node(self, name):
        return self._nodes.get(name)

    def has_node(self, name):
        return name in self._nodes

    def get_reverse_edge(self, edge):
        return edge.destination().edge_to(edge.source())

    def has_reverse_edge(self, edge):
        return self.get_reverse_edge(edge) is not None

    def _node_lookup(self, l):
        res = []
        for obj in l:
            if obj in self.nodes():
                res.append(obj)
            else:
                res.append(self._nodes.get(obj))

        return res if not len(res) == 1 else res[0]

    def __str__(self):
        res = "Nodes:\n"
        for node in self._nodes.values():
            res += str(node)

        res += "Edges:\n"
        for edge in self._edges:
            res += str(edge)

        return res