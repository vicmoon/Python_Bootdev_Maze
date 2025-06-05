from shapes import Cell 
import time
import random 

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
        seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        

        if seed is not None:
            random.seed(seed) 

        # Create a grid of cells
        self.__cells = []
        self.__create_cells()

        #break entrance and exit 

        self.__break_entrance_and_exit()

        # start the recursive function to carve the maze 

        self.__break_walls_r(0,0)


         # *** RESET all visited flags so we can solve the maze later ***
        self.__reset_cells_visited()



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

        # Because __cells[col][row], swap i and j here:
        cell = self.__cells[j][i]
        cell.draw(x_start, y_start, x_end, y_end)



    def _animate(self, delay=0.2):
        if self.win is not None:
            self.win.redraw()
            time.sleep(delay)

    def __break_entrance_and_exit(self):
        # Entrance : clear top wall of cells 

        top_left = self.__cells[0][0]
        top_left.has_top_wall = False 
        self._draw_cell(0,0)

        # Exit : clear bottom wall of cells 

        i = self.num_rows -1 
        j = self.num_cols -1
        bottom_right = self.__cells[j][i]
        bottom_right.has_bottom_wall = False
        self._draw_cell(i, j) 

    def __break_walls_r(self, i, j):
        # mark the current cell as visited 

        current = self.__cells[j][i]
        current.visited = True

        while True:
            #all unvisited neighbors 

            neighbors = []

            #up 

            if i > 0:
                up = self.__cells[j][i-1] 
                if not up.visited:
                    neighbors.append((i-1, j, "up"))

            #down

            if i < self.num_rows -1:
                down = self.__cells[j][i+1]
                if not down.visited:
                    neighbors.append((i+1, j, "down"))

            #left

            if j > 0:
                left = self.__cells[j-1][i]
                if not left.visited:
                    neighbors.append((i, j-1, "left"))

            #right

            if j < self.num_cols - 1:
                right = self.__cells[j+1][i]
                if not right.visited:
                    neighbors.append((i, j+1, "right"))

            # if no unvisited neighbors, break the loop

            if not neighbors:

                self._draw_cell(i, j)
                self._animate()
                return 
            
        # 4) Otherwise, choose one neighbor at random
            ni, nj, direction = random.choice(neighbors)

            # 5) Knock down the wall between (i, j) and (ni, nj)
            #   (a) If moving “up”, then remove current.top and neighbor.bottom
            if direction == "up":
                current.has_top_wall = False
                self.__cells[j][i - 1].has_bottom_wall = False

            #   (b) If moving “down”
            elif direction == "down":
                current.has_bottom_wall = False
                self.__cells[j][i + 1].has_top_wall = False

            #   (c) If moving “left”
            elif direction == "left":
                current.has_left_wall = False
                self.__cells[j - 1][i].has_right_wall = False

            #   (d) If moving “right”
            elif direction == "right":
                current.has_right_wall = False
                self.__cells[j + 1][i].has_left_wall = False

            # 6) After knocking down walls, redraw BOTH affected cells:
            self._draw_cell(i, j)        # redraw current cell with its walls updated
            self._draw_cell(ni, nj)      # redraw neighbor so its wall is also removed
            self._animate()              # animate this “step”

            # 7) Recurse into the chosen neighbor
            self.__break_walls_r(ni, nj)

            # 8) When recursion returns (we’re backtracking), 
            #    we can optionally draw a “backtrack move” or just continue the loop.
            #    In a plain DFS, we simply loop again to see if there are more neighbors left.
            
    
    def __reset_cells_visited(self):
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self.__cells[col][row].visited = False



















