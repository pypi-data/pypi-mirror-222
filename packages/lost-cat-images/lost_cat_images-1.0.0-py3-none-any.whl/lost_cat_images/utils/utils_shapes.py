"""This module will contain functions to handle image processing functions"""
import logging
import numpy as np
import math

logger = logging.getLogger(__name__)

def set_boundingbox(path: np.array):
    """calcualates the bounding box of a path"""
    x_coordinates, y_coordinates = zip(*path)
    return [(min(x_coordinates), min(y_coordinates)), (max(x_coordinates), max(y_coordinates))]

class BaseShape():
    """A base class to handle shapes
    Shapes have the following core attributes
        Bounding box = x, y, w, h
        Centroid - geometrc center of the shape
        Type - a best guess for the shape
        Path - a list of points that define the perimeters of the shape
        Smooth - a smoothed path for the edge
        Image - an np.array of the image (optional)
        isClosed - a flag to say the path is closed
        isConvex - the shape has convex paths
        tags - a set of labels

        # how the coord are given
        coord - [Top Left | Bottom Right | Bottom Left | Top Right]
        rounding - int | float | grid
    """
    def __init__(self, path: np.array = None, **kwargs):
        """initialize the class with defaults
        provide a set of key values will match based on the passed parameters"""
        if path is not None:
            self.path = path

        for key, value in kwargs.items():
            setattr(self, key, value)

        # check what was passed...
        convfuncs = {
            'int': (int, None),
            'float': (float, None),
            'grid': (round, 2),
        }
        if hasattr(self, 'rounding') :
            # we don't have the default format set
            self.confuncs = convfuncs.get(getattr(self, 'rounding'))
        else:
            self.rounding = 'int'
            self.confuncs = convfuncs.get('int')
        if not hasattr(self, 'confuncs'):
            self.rounding = 'int'
            self.confuncs = convfuncs.get('int')

        hasBBCount = 0
        for key in ["x", "y", "w", "h"]:
            if hasattr(self, key):
                hasBBCount += 1
        if hasBBCount < 4 and hasattr(self, 'path'):
            # no bounding box is set...
            (self.x, self.y, self.w, self.h) = set_boundingbox(getattr(path))

class Rectangle():
    """A class to wrap a rectangle, Top Left is (0,0)"""
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.center = (x + (w/2), y + (h/2))
        self.contains = [] # the rectangles pointers that are contined
        self.right = []     # the rectangles that have a right close right edge
        self.bottom = []    # the rectangles that have a overlapping close bottom edge

    def __repr__(self):
        """Text rep"""
        return f"Rectangle: X:{self.x} Y:{self.y} W:{self.w} H:{self.h}"

    def bbox(self):
        """Returns the bbox for the rectangle"""
        return self.x, self.y, self.w, self.h

    def add_tags(self, **kwargs) -> None:
        """Adds a tag to the object to allow for"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def data(self) -> dict:
        """Return the values in the class"""
        return vars(self)

def rectangle_contains(rect1: Rectangle, rect2: Rectangle) -> bool:
    """returns true if rect1 contains rect2, if it is the same size,
     it is not contained"""
    return (rect1.x < rect2.x) and (rect1.y < rect2.y) and (rect1.w + rect1.x > rect2.w + rect2.x) and (rect1.h + rect1.y > rect2.h + rect2.y)

def rectangle_intersect(rect1: Rectangle, rect2: Rectangle, border: int = 0) -> bool:
    """Check for intersect"""
    x_overlap = ((rect1.x - border) <= rect2.x <= (rect1.x + rect1.w + border)) or \
        ((rect1.x - border) <= (rect2.x + rect2.w) <= (rect1.x + rect1.w + border))
    y_overlap = ((rect1.y - border) <= rect2.y <= (rect1.y + rect1.h + border)) or \
        ((rect1.y - border) <= (rect2.y + rect2.h) <= (rect1.y + rect1.h + border))

    return x_overlap and y_overlap

def rectangle_distance(rect1: Rectangle, rect2: Rectangle) -> dict:
    """Check for radial distance of 2 rectangle,
    return a vector, and scalar
    return
    ------
    tuple: vector (x,y), distance
    """
    x_c1, y_c1 = rect1.center
    x_c2, y_c2 = rect2.center
    xmin = min(x_c1, x_c2)
    xmax = max(x_c1, x_c2)
    ymin = min(y_c1, y_c2)
    ymax = max(y_c1, y_c2)

    return ((x_c1-x_c2), (y_c1-y_c2)) , math.sqrt((xmax-xmin)^2 + (ymax-ymin)^2)

def rectangle_shared_edge(rect1: Rectangle, rect2: Rectangle, border: int = 0) -> dict:
    """Check for shared edges betwenn
    returns the shared edge.
    label and overpoints"""
    data = {}
    # Shared = TOP, LEFT,RIGHT, BOTTOM
    # overlap = Point 01, Point 02
    return data

def rectangle_merge(rect1: Rectangle, rect2: Rectangle) -> Rectangle:
    """Will return a rectangle that encloses both rectangles"""
    x = min(rect1.x, rect2.x)
    y = min(rect1.y, rect2.y)
    w = max(rect1.x + rect1.w, rect2.x + rect2.w) - x
    h = max(rect1.y + rect1.h, rect2.y + rect2.h) - y

    return Rectangle(x,y,w,h)

class ShapeGrouper():
    """This class will build a collection of objects"""
    def __init__(self):
        """initialize the core"""
        self.x = None
        self.y = None
        self.w = 0
        self.h = 0
        self.shapes = {
            "type": 'root',
            "shape": None,
            "children": []
        }
        self.rectangles = []

    def bbox(self):
        """Returns the bbox for the rectangle"""
        return self.x, self.y, self.w, self.h

    def add_rectangle(self, rect: Rectangle, options: dict = None):
        """will add the shape to the hierachy
            options:
                contains
                cluster
                    connected, width, height, tag, radius, vector
                vectors
                    [[x,y,radius]...]
        """
        useContains = options.get('contains', True) if options else True
        useCluster = 'cluster' in options if options else False
        cluser_type = options.get('cluster') if options else None
        vectors = options.get('vectors') if options else None

        # chech to see if is bounded...
        if root_rect := self.shapes.get('shape'):
            self.shapes['shape'] = rectangle_merge(root_rect, rect)
        else:
            x,y,w,h = rect.bbox()
            self.shapes['shape'] = Rectangle(x,y,w,h)

        # start at root...
        # for each child, if the incoming rect is larger that a child,
        # then that smaller child need added as children
        check_node = {
                "shape": rect,
                "type": "shape",
                "children": []
            }

        # scan the children and see if the node will fit here...
        logger.debug("Shapes: %s", self.shapes)

        if add_nodes := self.add_contains(node=self.shapes, check_node=check_node):
            logger.debug("Root Children: %s", add_nodes)
            self.shapes['children'] = add_nodes.copy()

        logger.debug("AddRect: Return: %s", self.shapes)
        self.rectangles.append(rect)

    def add_contains(self, node:dict, check_node:dict, depth:int = 1) -> dict:
        """Sorts the shapes into a containing hierarchy"""
        found = False
        resort = []
        children = []
        rect = check_node.get("shape")
        for child_node in node.get("children",[]):
            if test_rect := child_node.get("shape"):
                if rectangle_contains(rect, test_rect):
                    # incoming is larger
                    logger.debug("%sParent: %s > %s", "\t"*depth, rect, test_rect)
                    resort.append(child_node)

                elif found is False and rectangle_contains(test_rect, rect):
                    logger.debug("%sChild: %s > %s", "\t"*depth, test_rect, rect)
                    if add_nodes := self.add_contains(node=child_node,
                                check_node=check_node, depth=depth+1):
                        child_node["children"] = add_nodes.copy()
                        found = True

                        logger.debug("%sAdd All Children: %s", "\t"*depth, add_nodes)

                    else:
                        child_node["children"] = [check_node]
                        found = True

                        logger.debug("%sAdd First Child: %s", "\t"*depth, child_node)

                    children.append(child_node)
                else:
                    children.append(child_node)

        # the check node if not already added
        if found is False:
            # we didn't find a node to add to...
            logger.debug("%sAdding: %s", "\t"*depth, rect)
            children.append(check_node)
            found = True

        # add the resort node back into the tree
        grand_children = []
        for child_node in resort:
            logger.debug("%sResort: %s", "\t"*depth, child_node)
            # add these node into the tree below the check node
            if add_nodes := self.add_contains(node=check_node,
                        check_node=child_node, depth=depth+1):
                logger.debug("%sResort Found, %s", "\t"*depth, add_nodes)
                grand_children.extend(add_nodes.copy())
            else:
                children.append(child_node)

        check_node["children"].extend(grand_children)

        logger.debug("%sReadd: %s", "\t"*depth, len(children))
        return children

    def add_cluster(self, node:dict, rect:Rectangle, vectors:np.array) -> dict:
        """run though the containing nodes in the dict
        check each set of children,
        for each child that can be clustered with the test rectangle
            add to resort
            create a cluster rectangle to add to the current node
        otherwise
            keep as a child
        """
        found = False
        resort = []
        children = []
        for n in node.get("children",[]):
            test_rect = n.get("shape")

        return found

def printTree(obj:object, indent:int=0) -> list:
    """Prints to the hierarchy"""
    output = []
    if isinstance(obj,dict):
        for k,v in obj.items():
            output.append("{}:{}".format("\t"*indent, k))
            logger.info("%s:%s", "\t"*indent, k)
            output.extend(printTree(v,indent+1))
    elif isinstance(obj,list):
        for v in obj:
            output.extend(printTree(v,indent))
    else:
        output.append("{}:{}".format("\t"*indent, obj))
        logger.info("%s:%s", "\t"*indent, obj)
    return output

if __name__ == "__main__":
    logger.level = logging.DEBUG
    file_handler = logging.FileHandler("logs/utils_shapes.log")
    logger.addHandler(file_handler)

    coords = [
        # Rectangle x, y, w, h)
        Rectangle(2,2,9,9),
        Rectangle(3,3,4,4),
        Rectangle(1,1,11,11),
        Rectangle(1,1,2,1), # 3,2),
        Rectangle(3,5,4,1), # 7,6),
        Rectangle(3,6,4,1), # 7,7),
        Rectangle(3,7,4,1), # 7,8),
        Rectangle(3,8,2,2), # 5,10),
        Rectangle(7,5,3,3), # 10,8),
        Rectangle(5,8,5,2), # 10,10),
    ]

    shpg = ShapeGrouper()
    for rect in coords:
        shpg.add_rectangle(rect)

    op = printTree(shpg.shapes)
    for line in op:
        print(line)
    print()
