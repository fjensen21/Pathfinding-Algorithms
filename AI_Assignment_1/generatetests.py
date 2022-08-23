import random as rand
import math
import os
import shutil
import readin
from graph import Graph

COLS = 100
ROWS = 50
PERCENT_BLOCKED = 0.10
DIRNAME_FOR_SAVE = "automated_tests"


def generate_tests(n: int) -> None:
    """
    Given a number of test cases to generate, generates
    n grids with dimensions 100 cols 50 rows 10% of cells randomly blocked
    @param n: number of tests
    @return: generates test cases in a
    """

    # Create directory to store tests
    try:
        os.mkdir(DIRNAME_FOR_SAVE)
    except FileExistsError:
        print(f'Directory: {DIRNAME_FOR_SAVE} already exists.\nOverwriting it with new random testcases\n')
        shutil.rmtree(DIRNAME_FOR_SAVE)
        os.mkdir(DIRNAME_FOR_SAVE)

    # Generate tests and add them to directory as .txt files
    for i in range(n):
        cells = generate_vertices_dict(ROWS, COLS)
        # Pick 10% to block
        rand_keys = list(cells.keys())
        rand.shuffle(rand_keys)
        tenpercent = math.floor((COLS * ROWS) * PERCENT_BLOCKED)
        for j in range(tenpercent):
            cells[rand_keys[j]] = 1

        # Randomly pick a start node
        start_x = rand.randint(1, COLS + 1)
        start_y = rand.randint(1, ROWS + 1)

        # Randomly pick a goal node
        goal_x = rand.randint(1, COLS + 1)
        goal_y = rand.randint(1, ROWS + 1)

        with open(DIRNAME_FOR_SAVE + "/test" + str(i), 'w') as f:
            f.write(f'{start_x} {start_y}\n')
            f.write(f'{goal_x} {goal_y}\n')
            f.write(f'{COLS} {ROWS}\n')
            for key in cells:
                tokens = key.split("|")
                f.write(f'{tokens[0]} {tokens[1]} {cells[key]}\n')
        f.close()
        g = readin.read_in_graph(DIRNAME_FOR_SAVE + "/test" + str(i))

        while not is_valid_graph(g):
            with open(DIRNAME_FOR_SAVE + "/test" + str(i), 'w') as f:
                f.write(f'{start_x} {start_y}\n')
                f.write(f'{goal_x} {goal_y}\n')
                f.write(f'{COLS} {ROWS}\n')
                for key in cells:
                    tokens = key.split("|")
                    f.write(f'{tokens[0]} {tokens[1]} {cells[key]}\n')
            f.close()
            g = readin.read_in_graph(DIRNAME_FOR_SAVE + "/test" + str(i))

    print(f'{n} Test Files Generated\nLocation: {DIRNAME_FOR_SAVE}/\n')


def is_valid_graph(g: Graph) -> bool:
    """
    Runs BFS on a graph if it succeeds graph is valid. else graph is invalid
    @param g:
    @return:
    """

    start_node = g.getVertex(g.start_node_key)
    goal_node = g.getVertex(g.goal_node_key)

    visited = []
    frontier = []

    frontier.append(start_node)

    while frontier:
        m = frontier.pop()
        if m == goal_node:
            return True

        visited.append(m)
        for neighbor in m.getNeighbors():
            if neighbor not in visited:
                frontier.append(neighbor)

    return False


def generate_vertices_dict(r: int, c: int) -> dict:
    vertices = {}
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            key = str(j) + '|' + str(i)
            vertices[key] = 0

    return vertices


def h(s: tuple, g: tuple):
    return math.sqrt(2) * min(abs(s[0] - g[0]), abs(s[1] - g[1])) + max(abs(s[0] - g[0]), abs(s[1] - g[1])) - min(
        abs(s[0] - g[0]), abs(s[1] - g[1]))


if __name__ == '__main__':
    import sys

    generate_tests(int(sys.argv[1]))
