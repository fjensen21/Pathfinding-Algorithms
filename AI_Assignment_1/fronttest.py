import vertex
import graph
from griddisplay import *

test_graph = graph.Graph()

test_graph.addVertex(1)
test_graph.addVertex(2)
test_graph.addVertex(3)
test_graph.addVertex(4)

test_graph.getVertex(1).key = "100|100"
test_graph.getVertex(1).h = "1_h"
test_graph.getVertex(1).g = "1_g"
test_graph.getVertex(2).key = "100|200"
test_graph.getVertex(2).h = "2_h"
test_graph.getVertex(2).g = "2_g"
test_graph.getVertex(3).key = "200|100"
test_graph.getVertex(3).h = "3_h"
test_graph.getVertex(3).g = "3_g"
test_graph.getVertex(4).key = "200|200"
test_graph.getVertex(4).h = "4_h"
test_graph.getVertex(4).g = "4_g"

test_graph.addEdge("100|100", "100|200", 1)
test_graph.addEdge("100|100", "200|100", 1)
test_graph.addEdge("100|100", "200|200", 1)
test_graph.addEdge("100|200", "100|100", 1)
test_graph.addEdge("100|200", "200|200", 1)
test_graph.addEdge("100|200", "200|100", 1)
test_graph.addEdge("200|200", "100|200", 1)
test_graph.addEdge("200|200", "200|100", 1)
test_graph.addEdge("200|200", "100|100", 1)
test_graph.addEdge("200|100", "100|100", 1)
test_graph.addEdge("200|100", "200|200", 1)
test_graph.addEdge("200|100", "100|200", 1)

#root = Tk()
#canvas_name = Canvas(root, width=1000, height=1000)
#canvas_name.configure(bg="white")
#canvas_name.pack(fill="x", expand=True)

test_display = Display(test_graph) #creates a Display object
test_display.coordinate_producer() #produces the coordinates
test_display.bind_canvas() #this is what allows it to show up on screen
#the vertex info will be printed, it is not in the title anymore!!
