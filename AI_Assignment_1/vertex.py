class Vertex:

    def __init__(self, key):  # keys should be strings representing the coordinate Ex: (0,0) is entered as "0|0"
        self.key = key
        self.neighbors = {}  # vertex: weight
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None

    @classmethod
    def buildVertexKey(cls, x: int, y: int):
        x = int(x)
        y = int(y)
        return str(x) + "|" + str(y)

    def addNeighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

    def getNeighbors(self):
        # return self.neighbors.keys()
        return list(self.neighbors.keys())

    def getKey(self):
        return self.key

    def getHval(self):
        return self.h

    def getGval(self):
        return self.g

    def getFval(self):
        return self.f

    def getWeight(self, neighbor):
        return self.neighbors[neighbor]

    def getParent(self):
        return self.parent

    def getKeyCoordinates(self):
        """
        Returns the vertex's coordinates as a tuple (x,y)
        @return:
        """
        key_tokens = self.key.split("|")
        return (int(key_tokens[0]), int(key_tokens[1]))

    def setG(self, val):
        self.g = val
        self.f = self.g + self.h

    def setH(self, val):
        self.h = val
        self.f = self.g + self.h

    def __eq__(self, o: object) -> bool:
        return self.key == o.key

    def __str__(self):
        return self.key

    def __repr__(self):
        return self.key

    def __hash__(self):
        return hash(repr(self))

    def __lt__(self, other):
        return self.f < other.f


if __name__ == '__main__':
    pass
