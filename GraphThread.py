import threading
import time

class GraphThread(threading.Thread):

    #Too hard

    def __init__(self, graph, node, neighbors):
        threading.Thread.__init__(self)
        self.graph = graph
        self.node = node
        self.neighbor = neighbors