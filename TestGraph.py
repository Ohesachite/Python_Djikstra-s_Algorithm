# Main test file where I will be testing if my algorithm works
from Graph import Graph
if(__name__ == "__main__"):
    graph_elements1 = {
        "start": [("a", 7), ("b", 3)],
        "a": [("start", 7), ("b", 8), ("e", 4), ("stop", 20)],
        "b": [("start", 3), ("a", 8), ("e", 7), ("c", 12)],
        "c": [("b", 12), ("d", 5)],
        "d": [("c", 5), ("e", 6), ("f", 3)],
        "e": [("a", 4), ("b", 7), ("d", 6)],
        "f": [("d", 3), ("stop", 5)],
        "stop": [("a", 20), ("f", 5)]
    }

    graph_elements2 = {
        "start": [("a", 3), ("b", 2), ("c", 6)],
        "a": [("start", 3), ("d", 5), ("e", 7)],
        "b": [("start", 2), ("c", 5), ("d", 7)],
        "c": [("start", 6), ("b", 5), ("f", 7)],
        "d": [("a", 5), ("b", 7), ("f", 10), ("h", 9), ("j", 5)],
        "e": [("a", 7), ("g", 15)],
        "f": [("c", 7), ("d", 10), ("j", 3)],
        "g": [("e", 15), ("h", 9), ("i", 10)],
        "h": [("d", 9), ("g", 9), ("j", 6)],
        "i": [("g", 10), ("stop", 22)],
        "j": [("d", 5), ("f", 3), ("h", 6), ("stop", 43)],
        "stop": [("i", 22), ("j", 43)]
    }

    graph_elements3 = {
        "start": [("a", 1), ("stop", 100)],
        "a": [("start", 1), ("b", 1)],
        "b": [("a", 1)],
        "stop": [("start", 100)]
    }

    g1 = Graph(graph_elements1)
    g2 = Graph(graph_elements2)
    g3 = Graph(graph_elements3)

    # Method tests
    # print(g1.getVerticies())
    # print(g1.getEdges())
    # print(g1.getEdgeLengths())
    print(g1.shortestPath("start", "stop"))
    print(g2.shortestPath("start", "stop"))
    print(g3.shortestPath("start", "stop"))
