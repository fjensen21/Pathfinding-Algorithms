import math

from graph import Graph
import math as m
from vertex import Vertex


def generate_vertices(rows: int, cols: int, g: Graph) -> None:
    """
    Given a number of cell rows and columns, generates the appropriate amount of
    vertices. Note: if there are 4x3 cells there will be 5x4 vertices
    @param rows:
    @param cols:
    @param g:
    @return:
    """
    for i in range(1, rows + 2):
        for j in range(1, cols + 2):
            g.addVertex(Vertex.buildVertexKey(i, j))


def generate_outer_edges(rows: int, cols: int, g: Graph) -> None:
    """
    DEPRECIATED
    Generates outer straight edges does NOT generate inner diagonals
    @param rows:
    @param cols:
    @param g:
    @return: None
    """
    # Generates all horizontal edges
    for i in range(1, cols + 1):
        for j in range(1, rows + 1):
            fromV = Vertex.buildVertexKey(j, i)
            toV = Vertex.buildVertexKey(j + 1, i)
            g.addEdge(fromV, toV, 1)
            # print(f'({j},{i}) -- ({j + 1},{i})')

    # Generates all vertical edges
    for x in range(1, rows + 2):
        for y in range(1, cols + 1):
            fromV = Vertex.buildVertexKey(x, y)
            toV = Vertex.buildVertexKey(x, y + 1)
            g.addEdge(fromV, toV, 1)
            # print(f'({x},{y}) -- ({x},{y + 1})')


def add_diagonal_edges(cell_key: str, g: Graph) -> None:
    """
    DEPRECIATED
    Given the key for the left-topmost vertex in a cell,
    add both diagonals for the cell
    @param cell_key: a str cell key in the format 'xy'
    @param g:
    @return: None
    """
    cell_tokens = cell_key.split("|")
    x = int(cell_tokens[0])
    y = int(cell_tokens[1])
    fromV = cell_key
    toV = str(x + 1) + "|" + str(y + 1)

    g.addEdge(fromV, toV, m.sqrt(2))

    fromV = str(x + 1) + "|" + cell_tokens[1]
    toV = cell_tokens[0] + "|" + str(y + 1)

    g.addEdge(fromV, toV, m.sqrt(2))


def unblock_cell(cell_key: str, g: Graph):
    v1 = g.getVertex(cell_key)

    x = v1.getKeyCoordinates()[0]
    y = v1.getKeyCoordinates()[1]

    g.addEdge(cell_key, Vertex.buildVertexKey(x + 1, y), 1.0)
    g.addEdge(cell_key, Vertex.buildVertexKey(x, y + 1), 1.0)
    g.addEdge(cell_key, Vertex.buildVertexKey(x + 1, y + 1), math.sqrt(2))
    g.addEdge(Vertex.buildVertexKey(x + 1, y), Vertex.buildVertexKey(x, y + 1), math.sqrt(2))
    g.addEdge(Vertex.buildVertexKey(x + 1, y), Vertex.buildVertexKey(x + 1, y + 1), 1.0)
    g.addEdge(Vertex.buildVertexKey(x, y + 1), Vertex.buildVertexKey(x + 1, y + 1), 1.0)

def read_in_graph(filename: str):
    start_node = tuple()
    goal_node = tuple()
    grid_dimensions = tuple()
    g = Graph()

    with open(filename) as f:
        # Read start and goal node coords into a tuple
        line = f.readline().strip()
        tokens = line.split(" ")
        start_node = Vertex.buildVertexKey(int(tokens[0]), int(tokens[1]))
        g.start_node_key = start_node

        line = f.readline().strip()
        tokens = line.split(" ")
        goal_node = Vertex.buildVertexKey(int(tokens[0]), int(tokens[1]))
        g.goal_node_key = goal_node

        # Read grid dimensions into a tuple
        line = f.readline().strip()
        tokens = line.split(" ")
        grid_dimensions = (int(tokens[0]), int(tokens[1]))

        generate_vertices(grid_dimensions[0], grid_dimensions[1], g)
        # generate_outer_edges(grid_dimensions[0], grid_dimensions[1], g)

        for line in f:
            line = line.strip()
            tokens = line.split(" ")

            vertex_key = Vertex.buildVertexKey(int(tokens[0]), int(tokens[1]))
            g.cell_status[vertex_key] = int(tokens[2])

            if tokens[2] == '0':
                # add_diagonal_edges(str(tokens[0]) + "|" + str(tokens[1]), g)
                unblock_cell(Vertex.buildVertexKey(int(tokens[0]), int(tokens[1])), g)

    f.close()
    return g


if __name__ == '__main__':
    g = read_in_graph("automated_tests/test0")
    v = g.getVertex("1|1")
    neighbors = v.getNeighbors()
    print(neighbors)