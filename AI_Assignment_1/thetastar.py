import readin
import griddisplay
import math
from vertex import Vertex
import heapq

class ThetaStar:
    def __init__(self, graph):
        self.graph = graph
        self.fringe = []
        self.closed = []
        self.start_node = graph.getVertex(graph.start_node_key)
        self.goal_node = graph.getVertex(graph.goal_node_key)

    def main(self):
        self.start_node.setG(0)
        self.start_node.parent = self.start_node
        self.start_node.setH(self.h(self.start_node, self.goal_node))
        heapq.heappush(self.fringe, self.start_node)

        while len(self.fringe) > 0:
            s = heapq.heappop(self.fringe)
            if s == self.goal_node:
                return self.shortest_path(s)
            self.closed.append(s)
            for succ in s.getNeighbors():
                if succ not in self.closed:
                    if succ not in self.fringe:
                        succ.setG(math.inf)
                        succ.parent = None
                    self.UpdateVertex(s, succ)
        return None

    def UpdateVertex(self, s, succ):
        if self.LineOfSight(s.parent, succ):
            # Path 2
            if s.parent.g + self.c(s.parent, succ) < succ.g:
                succ.setG(self.c(s.parent, succ))
                succ.parent = s.parent
                if s in self.fringe:
                    self.fringe.remove(s)
                    heapq.heapify(self.fringe)
                succ.setH(self.h(succ, self.goal_node))
                heapq.heappush(self.fringe, succ)
        else:
            # Path 1
            if s.g + self.c(s, succ) < succ.g:
                succ.setG(s.g + self.c(s, succ))
                succ.parent = s
                if succ in self.fringe:
                    self.fringe.remove(succ)
                    heapq.heapify(self.fringe)
                succ.setH(self.h(succ, self.goal_node))
                heapq.heappush(self.fringe, succ)

    def g(self, node):
        """
        Returns the distance from start node
        @param node:
        @return:
        """
        g_total = 0;

        while node != self.start_node:
            p = node.getParent()
            g_total = g_total + node.getWeight(p)
            node = p
        return g_total

    def h(self, start_node: Vertex, goal_node: Vertex):
        s = start_node.getKeyCoordinates()
        g = goal_node.getKeyCoordinates()
        return math.sqrt(2) * min(abs(s[0] - g[0]), abs(s[1] - g[1])) + max(abs(s[0] - g[0]), abs(s[1] - g[1])) - min(
            abs(s[0] - g[0]), abs(s[1] - g[1]))

    def c(self, s, succ):
        return self.h(s, succ)

    def LineOfSight(self, s, succ):
        s_coords = s.getKeyCoordinates()
        succ_coords = succ.getKeyCoordinates()

        x0 = s_coords[0]
        y0 = s_coords[1]
        x1 = succ_coords[0]
        y1 = succ_coords[1]
        f = 0
        dy = y1-y0
        dx = x1-x0
        sy = 0
        sx = 0
        if dy < 0:
            dy = dy * -1
            sy = -1
        else:
            sy = 1
        if dx < 0:
            dx = -1 * dx
            sx = -1
        else:
            sx = 1

        if dx > dy:
            while x0 != x1:
                f = f + dy
                if f >= dx:
                    if self.CellIsBlocked(x0 + ((sx - 1)/2), y0+ ((sy - 1)/2)):
                        return False
                    y0 = y0 + sy
                    f = f - dx
                if f != 0 and self.CellIsBlocked(x0 + ((sx - 1)/2), y0 + ((sy - 1)/2)):
                    return False
                if dy == 0 and self.CellIsBlocked(x0 + ((sx - 1)/2), y0) and self.CellIsBlocked(x0 + ((sx - 1)/2), y0 - 1):
                    return False
                x0 = x0 + sx
        else:
            while y0 != y1:
                f = f + dx
                if f > dy:
                    if self.CellIsBlocked(x0 + ((sx - 1)/2), y0 + ((sy - 1))/2):
                        return False
                    x0 = x0 + sx
                    f = f - dy
                if f != 0 and self.CellIsBlocked(x0 + ((sx - 1)/2), y0 + ((sy - 1)/2)):
                    return False
                if dx == 0 and self.CellIsBlocked(x0, y0 + ((sy - 1)/2)) and self.CellIsBlocked(x0 - 1, y0 + ((sy - 1)/2)):
                    return False
                y0 = y0 + sy
        return True



    def CellIsBlocked(self, x, y):
        cell_key = Vertex.buildVertexKey(x, y)
        if self.graph.cell_status[cell_key] == 1:
            return True
        return False

    def shortest_path(self, end_node):
        path = []
        node = end_node
        while node != self.start_node:
            path.append(node)
            node = node.getParent()
        path.append(self.start_node)
        path.reverse()
        return path









if __name__ == '__main__':
    # gr = readin.read_in_graph('automated_tests/test0')
    # a = AStar(gr)
    #
    # print(a.g(gr.getVertex("4|1")))
    # display = griddisplay.Display(gr, 50, 7)
    # display.coordinate_producer()
    # display.bind_canvas()

    l = [2, 5, 8, 9, 1]
    heapq.heapify(l)
    print(l)
    l.pop()
    heapq.heapify(l)

