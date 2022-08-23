import tkinter
from tkinter import *
from graph import *
from vertex import Vertex
from draw import *


class Display:

    #root = Tk()
    #root.title = ("Click on vertices for info")
    #canvas_name = Canvas(root, width=1000, height=1000) #dimenisons of canvas should be sized better than this
    #canvas_name.configure(bg="white")
    #canvas_name.pack(fill="x", expand=True)

    def __init__(self, graph, scale, vertex_radius):
    #given graph object, sort of does canvas and root on its own
        self.graph = graph
        self.scale = scale
        self.vertex_radius = vertex_radius

        self.root = Tk()
        self.frame = Frame(self.root, width=500, height=500)
        self.frame.pack(expand=True, fill=BOTH)

        self.canvas_name = Canvas(self.frame, bg="white", width=500, height=500, scrollregion=(0, 0, 100*50*self.scale, 100*50*self.scale))
        # self.canvas_name = Canvas(self.frame, bg="white", width=500, height=500, scrollregion=(0, 0, 250000, 250000))

        self.scroll_y = Scrollbar(self.frame, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.configure(command=self.canvas_name.yview)

        self.scroll_x = Scrollbar(self.frame, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_x.configure(command=self.canvas_name.xview)

        self.canvas_name.configure(width=500, height=500)
        self.canvas_name.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.canvas_name.pack(side=LEFT, expand=True, fill=BOTH)

    def coordinate_producer(self):
    #calls methods to draw
        graph = self.graph
        canvas_name = self.canvas_name
        start_vertex = graph.getVertex(graph.start_node_key)
        goal_vertex = graph.getVertex(graph.goal_node_key)

        start_x, start_y = Vertex.getKeyCoordinates(start_vertex)
        start_x *= self.scale
        start_y *= self.scale
        goal_x, goal_y = Vertex.getKeyCoordinates(goal_vertex)
        goal_x *= self.scale
        goal_y *= self.scale

        points(start_x, start_y, self.canvas_name, self.vertex_radius+3, "start", "red") #to indicate the start and goal nodes
        points(goal_x, goal_y, self.canvas_name, self.vertex_radius+3, "goal", "red") #this is filled, so it goes before the other filled circles

        for vertex in graph: #goes through vertices

            x, y = Vertex.getKeyCoordinates(vertex)
            x *= self.scale
            y *= self.scale
            current_neighbors = vertex.getNeighbors()
            points(x, y, self.canvas_name, self.vertex_radius, "vertex", "black") #for a graph with vertices, but no edges

            if len(current_neighbors) != 0: #if there are edges
                for neighbor in current_neighbors:  #goes through a vertex's neighbors
                #PROBLEM: it will re-draw stuff
                    x_neigh, y_neigh = Vertex.getKeyCoordinates(neighbor)
                    x_neigh *= self.scale
                    y_neigh *= self.scale
                    points_and_lines(x, y, x_neigh, y_neigh, self)

        return


    def display_info(self, event):
    #Uses the mouse click location to determine which vertex + print appropriate info
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        info = ""

        for vertex in self.graph:
            vertex_x, vertex_y = Vertex.getKeyCoordinates(vertex)

            if self.scale*vertex_x in range(int(x - self.vertex_radius), int(x + self.vertex_radius)) and self.scale*vertex_y in range(int(y - self.vertex_radius), int(y + self.vertex_radius)):
            #if clicked coordinates are in the drawn vertex's range
                info = "This vertex's coordinates are " + str(vertex) + ", its g-value is " + str(vertex.g) + ", its h-value is " + str(vertex.h) + ", and its f-value is " + str(vertex.f)
                break
            else: #it's not going to reach this part
                info = "click on vertex, not line or blank space"

        print(info)
        return


    def bind_canvas(self):
    #<Button-1> is for mouse click, "vertex" is the tag of all vertices, display_info is what's run when vertex-tagged object is clicked
        self.canvas_name.tag_bind("vertex", "<Button-1>", self.display_info)
        self.root.mainloop() #displaying the stuff on the canvas
