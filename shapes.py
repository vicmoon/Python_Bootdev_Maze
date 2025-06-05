

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Line():
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def draw(self, canvas, fill_color="black", width=1):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=width)




class Cell():
    def __init__(self, window=None):
        # Track where to draw, and automatically detect the real canvas background color
        self.__window = window
        if self.__window:
            # Read the Canvas’s 'bg' option (e.g. "#000000" if black, "#ffffff" if white)
            self._bg = self.__window.canvas["bg"]
        else:
            self._bg = "white"

        # If the background is black, draw walls in white. Otherwise, draw walls in black.
        self._wall_color = "white" if self._bg in ("black", "#000000") else "black"

        # Initially, all four walls exist
        self.has_left_wall   = True
        self.has_right_wall  = True
        self.has_top_wall    = True
        self.has_bottom_wall = True

        # These store the last‐drawn pixel coordinates of this cell
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

        # Visited flag for carving/solving
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        # Update our internal coordinates so draw_move can find centers
        self.__x1, self.__y1 = x1, y1
        self.__x2, self.__y2 = x2, y2

        # Precompute endpoints for each wall segment
        wall_map = {
            'left':   ((x1, y1), (x1, y2)),
            'right':  ((x2, y1), (x2, y2)),
            'top':    ((x1, y1), (x2, y1)),
            'bottom': ((x1, y2), (x2, y2)),
        }

        # 1) LEFT edge
        (sx, sy), (ex, ey) = wall_map['left']
        if self.has_left_wall:
            color = self._wall_color    # draw wall in contrasting color
        else:
            color = self._bg            # erase by overdrawing in background color
        if self.__window:
            self.__window.draw_line(
                Line(Point(sx, sy), Point(ex, ey)),
                fill_color=color, width=1
            )

        # 2) RIGHT edge
        (sx, sy), (ex, ey) = wall_map['right']
        if self.has_right_wall:
            color = self._wall_color
        else:
            color = self._bg
        if self.__window:
            self.__window.draw_line(
                Line(Point(sx, sy), Point(ex, ey)),
                fill_color=color, width=1
            )

        # 3) TOP edge
        (sx, sy), (ex, ey) = wall_map['top']
        if self.has_top_wall:
            color = self._wall_color
        else:
            color = self._bg
        if self.__window:
            self.__window.draw_line(
                Line(Point(sx, sy), Point(ex, ey)),
                fill_color=color, width=1
            )

        # 4) BOTTOM edge
        (sx, sy), (ex, ey) = wall_map['bottom']
        if self.has_bottom_wall:
            color = self._wall_color
        else:
            color = self._bg
        if self.__window:
            self.__window.draw_line(
                Line(Point(sx, sy), Point(ex, ey)),
                fill_color=color, width=1
            )

    def draw_move(self, to_cell, undo=False):
        # Compute this cell’s center
        cx = (self.__x1 + self.__x2) / 2
        cy = (self.__y1 + self.__y2) / 2

        # Compute the target cell’s center
        tx = (to_cell._Cell__x1 + to_cell._Cell__x2) / 2
        ty = (to_cell._Cell__y1 + to_cell._Cell__y2) / 2

        # Red for forward, gray for backtracking
        color = "gray" if undo else "red"

        if self.__window:
            self.__window.draw_line(
                Line(Point(cx, cy), Point(tx, ty)),
                fill_color=color,
                width=2
            )
