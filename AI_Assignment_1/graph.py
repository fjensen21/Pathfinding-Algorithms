from vertex import Vertex

class Graph:
    def __init__(self):
        self.vertices = {}
        self.size = 0
        self.start_node_key = ""
        self.goal_node_key = ""
        self.cell_status = {}  # key: str, val: int

    def addVertex(self, key):
        self.size += 1
        temp = Vertex(key)
        self.vertices[key] = temp
        return temp

    def getVertex(self, key) -> Vertex:
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def addEdge(self, startV: str, endV: str, weight):  # takes keys not vertex objects
        """
        Adds undirected edges so edges are placed from both vertices
        @param startV:
        @param endV:
        @param weight:
        @return:
        """
        if startV not in self.vertices:
            self.addVertex(startV)
        if endV not in self.vertices:
            self.addVertex(endV)

        self.vertices[startV].addNeighbor(self.vertices[endV], weight)
        self.vertices[endV].addNeighbor(self.vertices[startV], weight)

    def getVertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def __contains__(self, item):
        if item in self.vertices:
            return True
        else:
            return False


if __name__ == '__main__':
    g = Graph()
