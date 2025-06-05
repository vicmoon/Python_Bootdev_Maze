

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
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

        self.__window = window
        self._bg = "white"   # set to background color (white)

        self.visited = False 

    def draw(self, x1, y1, x2, y2):
        self.__x1, self.__y1 = x1, y1
        self.__x2, self.__y2 = x2, y2

        wall_map = {
            'left':   ((x1, y1), (x1, y2)),
            'right':  ((x2, y1), (x2, y2)),
            'top':    ((x1, y1), (x2, y1)),
            'bottom': ((x1, y2), (x2, y2)),
        }

        # always draw each edge, using bg color if wall is removed
        # left edge
        (sx, sy), (ex, ey) = wall_map['left']
        color = "black" if self.has_left_wall else self._bg
        if self.__window:
            self.__window.draw_line(Line(Point(sx, sy), Point(ex, ey)), fill_color=color, width=1)

        # right edge
        (sx, sy), (ex, ey) = wall_map['right']
        color = "black" if self.has_right_wall else self._bg
        if self.__window:
            self.__window.draw_line(Line(Point(sx, sy), Point(ex, ey)), fill_color=color, width=1)

        # top edge
        (sx, sy), (ex, ey) = wall_map['top']
        color = "black" if self.has_top_wall else self._bg
        if self.__window:
            self.__window.draw_line(Line(Point(sx, sy), Point(ex, ey)), fill_color=color, width=1)

        # bottom edge
        (sx, sy), (ex, ey) = wall_map['bottom']
        color = "black" if self.has_bottom_wall else self._bg
        if self.__window:
            self.__window.draw_line(Line(Point(sx, sy), Point(ex, ey)), fill_color=color, width=1)


