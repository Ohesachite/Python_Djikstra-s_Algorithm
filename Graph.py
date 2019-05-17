class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def getVerticies(self):
        return list(self.gdict.keys())

    def getVertexByIndex(self, index):
        return self.getVerticies()[index]

    def getIndexByVertex(self, vertex):
        result = 0
        for v in self.getVerticies():
            if v == vertex:
                return result
            else:
                result += 1
        return None

    def getEdges(self):
        # edgesSet allows filtering of duplicates
        edgesSet = []
        # seperate tuple list for return and usability in getEdgeLengths
        edges = []
        for vertex in self.gdict:
            for nextvertex in self.gdict[vertex]:
                if {nextvertex[0], vertex} not in edgesSet:
                    edgesSet.append({vertex, nextvertex[0]})
                    edges.append((vertex, nextvertex[0]))
        return edges

    def getEdgeLengths(self):
        edgeLens = []
        edges = self.getEdges()
        for edge in edges:
            for vertex in self.gdict[edge[0]]:
                if vertex[0] is edge[1]:
                    edgeLens.append(vertex[1])
        return edgeLens

    def hasPath(self, start, stop, visited):
        visited[self.getIndexByVertex(start)] = True
        if start == stop:
            return True
        elif len(self.getUnvisitedNeighbors(start, visited)) == 0:
            return False
        else:
            result = False
            for vertex in self.getUnvisitedNeighbors(start, visited):
                if self.hasPath(vertex[0], stop, visited) is True:
                    result = True
            return result

    # Takes two strings as parameters
    # Dijkstra's Algorithm
    def shortestPath(self, start, stop):

        q = self.getVerticies()

        assert len(q) > 0, "Graph must have at least one nodes"
        for e in self.getEdgeLengths():
            assert e >= 0, "Cannot have negative edge lengths"
        v = []
        for _ in q:
            v.append(False)
        assert self.hasPath(start, stop, v) is True, "No path exists"

        dist = []
        visited = []
        for vertex in q:
            if vertex == start:
                dist.append(0)
            else:
                dist.append(100**100)
            visited.append(False)

        for _ in range(len(q)):
            verInd = self.lowestUnvisitedDistanceIndex(dist, visited)
            neighbors = self.getUnvisitedNeighbors(self.getVertexByIndex(verInd), visited)
            # Keep in mind that neighbor is a TUPLE
            # - containing a string representing the vertex
            # - and an int representing the distance from the vertex parameter
            for neighbor in neighbors:
                nInd = self.getIndexByVertex(neighbor[0])
                if dist[verInd] + neighbor[1] < dist[nInd]:
                    dist[nInd] = dist[verInd] + neighbor[1]

            visited[verInd] = True

        # Proof of correctness by induction

        v = []
        for _ in q:
            v.append(False)

        for _ in range(len(q)):
            # Base Case
            verInd = self.lowestUnvisitedDistanceIndex(dist, v)
            if self.getVertexByIndex(verInd) == start:
                assert dist[self.getIndexByVertex(start)] == 0, "Algorithm not correct, base case is incorrect"
                v[verInd] = True
            else:
                # lowestDistInd gets the index of the unvisited node with the lowest distance from the start
                # The inductive step gets the closest neighbor
                # And checks that the distance from the closest neighbor plus the distance from that neighbor to the start is greater than or equal to the node's distance from the start
                uNeighbors = self.getVisitedNeighbors(self.getVertexByIndex(verInd), v)

                # Find closest visited node in terms of distance
                closestDistance = 100**100
                closestNode = None
                for u in uNeighbors:
                    if u[1] < closestDistance:
                        closestNode = u[0]
                        closestDistance = u[1]

                # Inductive Step
                assert dist[self.getIndexByVertex(closestNode)] + closestDistance >= dist[verInd]

        return dist[self.getIndexByVertex(stop)]

    def shortestPathMultithreaded(self, start, stop):

        # Nope too hard

        return

    # Helper method which calculates the lowest index node not visited
    def lowestUnvisitedDistanceIndex(self, distances, visited):
        result = 0
        resVal = 100**100
        for i in range(len(distances)):
            if distances[i] < resVal and visited[i] is False:
                result = i
                resVal = distances[i]
        return result

    # Helper method which gets unvisited neighbors
    # Keep in mind that vertex is a string
    # Also keep in mind that this returns a list of TUPLES
    # - containing a string representing the vertex
    # - and an int representing the distance from the vertex parameter
    def getUnvisitedNeighbors(self, vertex, visited):
        unvisited = []
        for neighbor in self.gdict[vertex]:
            if visited[self.getIndexByVertex(neighbor[0])] is False:
                unvisited.append(neighbor)
        return unvisited

    def getVisitedNeighbors(self, vertex, visited):
        result = []
        for neighbor in self.gdict[vertex]:
            if visited[self.getIndexByVertex(neighbor[0])] is True:
                result.append(neighbor)
        return result