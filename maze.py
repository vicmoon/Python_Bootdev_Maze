from shapes import Cell 
import time

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        # Create a grid of cells
        self.__cells = []

        self.__create_cells()

    def __create_cells(self):
    # build columns of rows:
        for col in range(self.num_cols):
            col_list = []
            for row in range(self.num_rows):
                # compute pixel corners
                x0 = self.x1 + col * self.cell_size_x
                y0 = self.y1 + row * self.cell_size_y
                x1 = x0 + self.cell_size_x
                y1 = y0 + self.cell_size_y

                # 1) instantiate a Cell with only the window
                cell = Cell(self.win)

                # 2) tell it to draw itself in that box
                cell.draw(x0, y0, x1, y1)

                col_list.append(cell)
            self.__cells.append(col_list)


    def _draw_cell(self, i, j):
        x_start = self.x1 + j * self.cell_size_x
        y_start = self.y1 + i * self.cell_size_y
        x_end = x_start + self.cell_size_x
        y_end = y_start + self.cell_size_y
        cell = self.cells[i][j]
        cell.draw(x_start, y_start, x_end, y_end)



    def _animate(self, delay=0.2):
        self.__win.redraw()
        time.sleep(delay)

    def __break_entrance_and_exit(self):
        # Entrance : clear top wall of cells 

        top_left = self.cells[0][0]
        top_left.has_top_wall = False 
        self._draw_cell(0,0)

        # Exit : clear bottom wall of cells 

        i = self.num_rows -1 
        j = self.num_cols -1
        bottom_right = self.cells[i][j]
        bottom_right.has_bottom_wall = False
        self._draw_cell(i, j) 









