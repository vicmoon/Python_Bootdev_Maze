from theCanvas import MyWindow
from maze      import Maze

def main():
    window = MyWindow()

    # 1. Build the maze (no carving yet)
    maze = Maze(
        x1=20, y1=20,
        num_rows=11, num_cols=17,
        cell_size_x=50, cell_size_y=50,
        win=window
    )

    # 2. Carve entrance/exit & interior walls
    maze._Maze__break_entrance_and_exit()
    maze._Maze__break_walls_r(0, 0)

    # 3. Reset visited flags before solving
    maze._Maze__reset_cells_visited()

    # 4. Solve the maze (draw red/gray moves)
    solved = maze.solve()
    print(f"Maze solved? {solved}")

    # 5. Hand control to the window loop so it stays open
    window.wait_for_close()

# 6. Actually call main() when this file is run:
if __name__ == "__main__":
    main()
