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

    # Takes two strings as parameters
    # Djikstra's Algorithm
    def shortestPath(self, start, stop):

        q = self.getVerticies()

        dist = []
        visited = []
        for vertex in q:
            if(vertex == start):
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

        return dist[self.getIndexByVertex(stop)]

    #Helper method which calculates the lowest index node not visited
    def lowestUnvisitedDistanceIndex(self, distances, visited):
        result = 0
        resVal = 100**100
        for i in range(len(distances)):
            if distances[i] < resVal and visited[i] == False:
                result = i
                resVal = distances[i]
        return result

    #Helper method which gets unvisited neighbors
    # Keep in mind that vertex is a string
    # Also keep in mind that this returns a list of TUPLES
    # - containing a string representing the vertex
    # - and an int representing the distance from the vertex parameter
    def getUnvisitedNeighbors(self, vertex, visited):
        unvisited = []
        for neighbor in self.gdict[vertex]:
            if visited[self.getIndexByVertex(neighbor[0])] == False:
                unvisited.append(neighbor)
        return unvisited