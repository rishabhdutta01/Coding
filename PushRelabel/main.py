from graph import *
from pushRelabel import *

if __name__ == '__main__':
    g = Graph()

    #Easy Ahuja book
    # g.add_nodes(["S", "A", "B", "T"])
    # g.add_edge("S", "A", {"capacity": 2})
    # g.add_edge("S", "B", {"capacity": 4})
    # g.add_edge("A", "T", {"capacity": 1})
    # g.add_edge("A", "B", {"capacity": 3})
    # g.add_edge("B", "T", {"capacity": 5})

    #Corman
    g.add_nodes(["S", "A", "B", "C", "D", "T"])
    g.add_edge("S", "A", {"capacity": 16})
    g.add_edge("S", "B", {"capacity": 13})
    g.add_edge("A", "C", {"capacity": 12})
    g.add_edge("C", "B", {"capacity": 9})
    g.add_edge("C", "T", {"capacity": 20})
    g.add_edge("B", "A", {"capacity": 4})
    g.add_edge("B", "D", {"capacity": 14})
    g.add_edge("D", "C", {"capacity": 7})
    g.add_edge("D", "T", {"capacity": 4})

    preflowAlgo(g, g.get_node("S"), g.get_node("T"))
    print(g)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
