import sys

import astar
import draw
import readin
import griddisplay
import thetastar


def main():

    graph_file, algo = sys.argv[1], sys.argv[2]
    graph = readin.read_in_graph(graph_file)

    display = griddisplay.Display(graph, 50, 7)
    display.coordinate_producer()

    shortest_path = []

    if algo.lower() == 'a':
        shortest_path = astar.AStar(graph).main()
    elif algo.lower() == 't':
        shortest_path = thetastar.ThetaStar(graph).main()

    draw.draw_path(display, shortest_path, "red")

    display.bind_canvas()

def debug(graph_file, algo):

    graph = readin.read_in_graph(graph_file)

    display = griddisplay.Display(graph, 50, 7)
    display.coordinate_producer()

    shortest_path = []

    if algo.lower() == 'a':
        shortest_path = astar.AStar(graph).main()
    elif algo.lower() == 't':
        shortest_path = thetastar.ThetaStar(graph).main()

    draw.draw_path(display, shortest_path, "red")

    display.bind_canvas()


if __name__ == '__main__':
    # debug("automated_tests/test3", 't')
    main()