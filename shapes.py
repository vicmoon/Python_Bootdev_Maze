

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
        self._bg = "black"  # background color for the cell, default is black


    def draw(self, x1, y1, x2, y2):
        # 1) update your internal coords
        self.__x1, self.__y1 = x1, y1
        self.__x2, self.__y2 = x2, y2

        # 2) prepare the endpoints for each wall
        wall_map = {
            'left':   ((x1, y1), (x1, y2)),
            'right':  ((x2, y1), (x2, y2)),
            'top':    ((x1, y1), (x2, y1)),
            'bottom': ((x1, y2), (x2, y2)),
        }

        # 3) draw each wall if its flag is True
        if self.has_left_wall:
            # unpack the two endpoint tuples
            (sx, sy), (ex, ey) = wall_map['left']
            color = "black" if self._bg == "black" else "white"
            p_start = Point(sx, sy)
            p_end   = Point(ex, ey)
            line_obj = Line(p_start, p_end)
            # use your window’s draw_line (so it gets recorded for redraws)
            if self.__window is not None:
                self.__window.draw_line(line_obj, fill_color=color, width=1)
            

        if self.has_right_wall:
            (sx, sy), (ex, ey) = wall_map['right']
            color = "black" if self._bg == "black" else "white"
            p_start = Point(sx, sy)
            p_end   = Point(ex, ey)
            line_obj = Line(p_start, p_end)
            if self.__window is not None:
                self.__window.draw_line(line_obj, fill_color=color, width=1)

        if self.has_top_wall:
            (sx, sy), (ex, ey) = wall_map['top']
            color = "black" if self._bg == "black" else "white"
            p_start = Point(sx, sy)
            p_end   = Point(ex, ey)
            line_obj = Line(p_start, p_end)
            if self.__window is not None:
                self.__window.draw_line(line_obj, fill_color=color, width=1)

        if self.has_bottom_wall:
            (sx, sy), (ex, ey) = wall_map['bottom']
            color = "black" if self._bg == "black" else "white"
            p_start = Point(sx, sy)
            p_end   = Point(ex, ey)
            line_obj = Line(p_start, p_end)
            if self.__window is not None:
                self.__window.draw_line(line_obj, fill_color=color, width=1)


    def draw_move(self, to_cell, undo=False):
        # compute centers
        cx = (self.__x1 + self.__x2) / 2
        cy = (self.__y1 + self.__y2) / 2
        tx = (to_cell.__x1 + to_cell.__x2) / 2
        ty = (to_cell.__y1 + to_cell.__y2) / 2

        #  color 
        color = "gray" if undo else "red" 

        # draw a line between the two centers

        start = Point(cx, cy)
        end = Point(tx, ty)
        move = Line(start, end)
        if self.__window is not None:
            self.__window.draw_line(move, fill_color=color, width=2)








