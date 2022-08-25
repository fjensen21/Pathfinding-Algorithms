# NOT WRITTEN BY FINN JENSEN #

from vertex import Vertex

def points(x, y, canvas_name, radius, tag, fill):
#Given coordinates and the canvas name, it draws (and tags) the vertices
    r = radius #radius—can be changed if the circles need to be bigger
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas_name.create_oval(x0, y0, x1, y1, fill=fill, tag=tag)
    #the tag could be changed to be a specific vertex name if needed, probably unnecessary


def lines(x1, y1, x2, y2, pass_display, fill):
#Given 4 coordinates (for 2 points), draws a line between them. Also passed canvas name and a string for line color
    canvas = pass_display.canvas_name
    canvas.create_line(x1, y1, x2, y2, fill=fill)
    return


def points_and_lines(x1, y1, x2, y2, pass_display):
#Given 2 vertices and a canvas name, draws all points and lines between the two vertices
    lines(x1, y1, x2, y2, pass_display, "black")
    #points(x1, y1, canvas_name, "vertex", "black", 5)
    points(x2, y2, pass_display.canvas_name, pass_display.vertex_radius, "vertex", "black")
    return


def split_coordinates(s: str):
#same as the method "getKeyCoordinates" in the Vertex class. however, that works with vertices, this is in the case that strings are passed and not vertices
    # x_coord = ""
    # y_coord = ""
    # is_x = True
    # char_coords = [char for char in string]
    #
    # for c in char_coords:
    #     if c == '|':
    #         is_x = False
    #         #y_coord += c
    #     elif is_x:
    #         x_coord += c
    #     else:
    #         y_coord += c
    #
    # coord_list = [int(x_coord), int(y_coord)]

    tokens = s.split("|")
    coord_list = list(int(tokens[0]), int(tokens[1]))
    return coord_list


def draw_path(pass_display, path_list, fill):

    for i in range(0, len(path_list) - 1):
        x1, y1 = path_list[i].getKeyCoordinates()
        x2, y2 = path_list[i + 1].getKeyCoordinates()
        x1 *= pass_display.scale
        y1 *= pass_display.scale
        x2 *= pass_display.scale
        y2 *= pass_display.scale
        lines(x1, y1, x2, y2, pass_display, fill)
